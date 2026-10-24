# LdmPipelineLoader

## 节点类型

`LdmPipelineLoader`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `ckpt_name:COMBO`（1 次）
- `pipeline_name:COMBO`（1 次）

## 输出

- `PIPELINE:PIPELINE`（3 次）
- `AUTOENCODER:AUTOENCODER`（3 次）
- `SCHEDULER:SCHEDULER`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["juggernautXL_juggXIByRundiffusion.safetensors", "MVAdapterI2MVSDXLPipeline"]`（1 次）
- `["MR 3DQ _SDXL V0.2.safetensors", "MVAdapterI2MVSDXLPipeline"]`（1 次）
- `["DynaVision XL - All-in-one stylized 3D_0.5.7.7.safetensors", "MVAdapterI2MVSDXLPipeline"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
