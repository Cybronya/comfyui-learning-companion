# easy sam3VideoModelExtraConfig

## 节点类型

`easy sam3VideoModelExtraConfig`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `assoc_iou_thresh:FLOAT`（13 次）
- `det_nms_thresh:FLOAT`（13 次）
- `new_det_thresh:FLOAT`（13 次）
- `hotstart_delay:INT`（13 次）
- `hotstart_unmatch_thresh:INT`（13 次）
- `hotstart_dup_thresh:INT`（13 次）
- `suppress_unmatched_within_hotstart:BOOLEAN`（13 次）
- `min_trk_keep_alive:INT`（13 次）
- `max_trk_keep_alive:INT`（13 次）
- `init_trk_keep_alive:INT`（13 次）

## 输出

- `extra_config:EASY_SAM3_EXTRA_CONFIG`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0.1, 0.1, 0.7, 15, 8, 8, true, -1, 30, 30, 0.7, false, 16, 16, false, false, 1008]`（13 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
