# FeishuFetchVideoNode

## 节点类型

`FeishuFetchVideoNode`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `飞书配置:FEISHU_CONFIG`（1 次）
- `目标列名:STRING`（1 次）
- `筛选条件:STRING`（1 次）
- `视频索引:INT`（1 次）
- `提取列名:STRING`（1 次）
- `列分隔符:STRING`（1 次）

## 输出

- `视频:VIDEO`（1 次）
- `状态信息:STRING`（1 次）
- `提取的内容:STRING`（1 次）
- `使用说明:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["视频", "ID+1", 1, "", " | "]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
