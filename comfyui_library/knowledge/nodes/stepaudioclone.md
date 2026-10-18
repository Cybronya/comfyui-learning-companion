# StepAudioClone

## 节点类型

`StepAudioClone`

## 分类

Audio

## 作用

音频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `clone_audio:AUDIO`（3 次）
- `text:STRING`（2 次）
- `clone_text:STRING`（2 次）

## 输出

- `audio:AUDIO`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Myvoice", "大哥怕是忘了小妹的能耐，有兴趣做个交易吗？", "None", "中文", "None", "快速1", ""]`（1 次）
- `["", "Myvoice", "大哥怕是忘了小妹的能耐，有兴趣做个交易吗？", "None", "中文", "None", "None", "(温柔)"]`（1 次）
- `["月落乌啼霜满天，\n江枫渔火对愁眠，\n姑苏城外寒山寺，\n夜半钟声到客船。", "无名", "", "None", "None", "None", "None", "", [false, true], [false, true]]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
