# DirectorAudioScriptLoader

## 节点类型

`DirectorAudioScriptLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `audio_json:STRING`（3 次）

## 输出

- `角色列表(Role):STRING`（3 次）
- `音色提示词(Instruct):STRING`（3 次）
- `纯台词(Text):STRING`（3 次）
- `总场数:INT`（3 次）
- `索引列表(Loop):INT`（3 次）
- `角色字典(Dict):DICT`（3 次）
- `角色设定详情(String):STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[]`（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
