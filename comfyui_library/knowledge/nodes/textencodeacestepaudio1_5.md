# TextEncodeAceStepAudio1.5

## 节点类型

`TextEncodeAceStepAudio1.5`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `clip:CLIP`（6 次）
- `seed:INT`（6 次）
- `duration:FLOAT`（6 次）

## 输出

- `CONDITIONING:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["A quiet, meditative ambient electronic track at 72 BPM in 4/4 time. The piece opens with slowly evolving pad textures `（1 次）
- `["A lush neo-soul track anchored by a warm Rhodes electric piano playing rich ninth and thirteenth chords over a loose, `（1 次）
- `["Late Night Trap, 95 BPM, Heavy 808 Bass, Wet Synths, Female Background Vocals, Male Rap Vocals + Seductive Female Voca`（1 次）
- `["Neo-Soul: A warm, organic neo-soul track dripping with live instrumentation and effortless groove. A live drummer play`（1 次）
- `["K-Pop: A slick, maximalist K-pop track that genre-hops with precision and style. The production shifts seamlessly betw`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
