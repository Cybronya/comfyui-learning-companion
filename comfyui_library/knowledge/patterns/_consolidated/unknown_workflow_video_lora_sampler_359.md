---
name: unknown_workflow_video_lora_sampler_359
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.879
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json, 视频生成/图生视频/kone专属图生视频_2007088250229366786.json, 视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json, 视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json, 视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json, 视频生成/图生视频/wan2_2_子弹时间 极速版_1984472483812229122.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_359

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.2图生视频超级加速_1955793674186604546.json、视频生成/图生视频/kone专属图生视频_2007088250229366786.json、视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json、视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json、视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 5/6 个有
- `ModelPatchTorchSettings` —— 5/6 个有
- `CR SDXL Aspect Ratio` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 6 | 6 | 80% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 6，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
