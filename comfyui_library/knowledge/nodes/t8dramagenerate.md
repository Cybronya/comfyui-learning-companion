# T8DramaGenerate

## 节点类型

`T8DramaGenerate`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `engine:DRAMA3_T8_ENGINE`（2 次）
- `session:DRAMA3_T8_SESSION`（2 次）
- `mode:COMBO`（2 次）
- `text:STRING`（2 次）
- `lookahead:STRING`（2 次）
- `chunk_bytes:INT`（2 次）
- `seed:INT`（2 次）
- `temperature:FLOAT`（2 次）
- `top_p:FLOAT`（2 次）
- `top_k:INT`（2 次）

## 输出

- `DRAMA3_T8_SESSION:DRAMA3_T8_SESSION`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["speech", "你好，这是本地语音测试。", "", 300, 42, "fixed", 0.7, 0.7, 30, 180, "", 0, "custom"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
