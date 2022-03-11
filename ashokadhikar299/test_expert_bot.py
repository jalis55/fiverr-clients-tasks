def test_match():

    # the match function should return True, since the domain is `splunk`
    assert plugin.match({"text": "I have a question on Splunk query"}) is True
    assert plugin.match({"text": "Question on the following splunk query"}) is True
    assert (
        plugin.match(
            {"text": "Can some help me what's wrong with the following splunk query?"}
        )
        is True
    )

    # the match function should return True, since the domain is `spark`
    assert plugin.match({"text": "I have a question on Spark streaming job"}) is True
    assert plugin.match({"text": "Question on the following spark code"}) is True
    assert (
        plugin.match(
            {"text": "Can some help me what's wrong with the following spark logic?"}
        )
        is True
    )

    # the match function should return False, since the domain is `clojure` and we don't have people
    # associated with this domain yet
    assert plugin.match({"text": "I have a question on clojure"}) is False


def test_handle():
    assert (
        plugin.handle({"text": "I have a question on Splunk query"})
        == "@PersonA to see if he can help this Splunk question"
    )
    assert (
        plugin.handle({"text": "Question on the following splunk query"})
        == "@PersonA to see if he can help this Splunk question"
    )

    assert (
        plugin.handle({"text": "Question on the following spark code"})
        == "@PersonB to see if she can help this Spark question"
    )
    assert (
        plugin.handle(
            {"text": "Can some help me what's wrong with the following spark logic?"}
        )
        == "@PersonB to see if she can help this Spark question"
    )
