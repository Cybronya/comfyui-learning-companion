# HAIGC_TimestampTextReplace

## 节点类型

`HAIGC_TimestampTextReplace`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `时间戳文本:STRING`（1 次）
- `时间戳格式:COMBO`（1 次）
- `替换模式:COMBO`（1 次）
- `替换文本:STRING`（1 次）
- `关键字_正则:STRING`（1 次）
- `指定段落索引:STRING`（1 次）
- `文本增强选项:COMBO`（1 次）
- `前缀_后缀内容:STRING`（1 次）
- `智能分段策略:COMBO`（1 次）
- `保留空行:COMBO`（1 次）

## 输出

- `处理后的时间戳文本:STRING`（1 次）
- `处理报告:STRING`（1 次）
- `段落数:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "自动检测", "批量替换(按时间排序)", "", "", "1,2,3", "无", "", "按行分段", "否", "是", "保持原格式", "否"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
