# YUAN_TXTJsonExtractor

## 节点类型

`YUAN_TXTJsonExtractor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `json:*`（7 次）
- `开关配置:*`（7 次）
- `情节衔接文本:*`（7 次）
- `索引:INT`（7 次）
- `档案选择:COMBO`（7 次）
- `BGM开关:BOOLEAN`（3 次）

## 输出

- `整体风格:STRING`（7 次）
- `档案:STRING`（7 次）
- `档案编码:INT`（7 次）
- `分镜序列:STRING`（7 次）
- `角色索引:STRING`（7 次）
- `音色索引:STRING`（7 次）
- `道具索引:STRING`（7 次）
- `场景索引:STRING`（7 次）
- `索引时长:FLOAT`（7 次）
- `场景上下文:BOOLEAN`（7 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1, "场景档案"]`（3 次）
- `[1, "角色档案"]`（2 次）
- `[1, "道具档案"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
