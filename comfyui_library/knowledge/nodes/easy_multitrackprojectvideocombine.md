# easy multitrackProjectVideoCombine

## 节点类型

`easy multitrackProjectVideoCombine`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `project_name:STRING`（2 次）
- `project_data:PROJECT_DATA`（2 次）

## 输出

- `VIDEO:VIDEO`（2 次）
- `FILENAME_PREFIX:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["{\"project_name\":\"default\",\"width\":768,\"height\":1376,\"frame_rate\":24,\"clips\":[{\"id\":\"segment-0\",\"index`（1 次）
- `["{\"project_name\":\"666\",\"width\":1280,\"height\":736,\"frame_rate\":24,\"clips\":[],\"auto_combine\":true,\"updated`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
