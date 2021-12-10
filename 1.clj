(require '[clojure.string :as str])

(defn parse [file]
  (map #(Integer/parseInt %) (str/split-lines (slurp file))))

(defn part-one [arr]
  (reduce #(if (> %2 (last %1))
             [(inc (first %1)) %2]
             [(first %1) %2])
          [0 (first arr)]
          arr))

(part-one (parse "data/1.txt"))
