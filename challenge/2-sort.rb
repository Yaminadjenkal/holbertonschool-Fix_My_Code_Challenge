#!/usr/bin/env ruby

###
#  Sort integer arguments (ascending)
###

result = []

ARGV.each do |arg|
    # Vérifier si l'argument est un entier
    next unless arg.match?(/^[-]?\d+$/)

    # Convertir en entier
    i_arg = arg.to_i

    # Insérer le nombre à la bonne position
    is_inserted = false
    i = 0
    l = result.size

    while !is_inserted && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg)
            is_inserted = true
            break
        end
    end

    result << i_arg unless is_inserted
end

# Afficher les nombres triés
puts result
