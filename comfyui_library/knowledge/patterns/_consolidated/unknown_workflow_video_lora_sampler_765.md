---
name: unknown_workflow_video_lora_sampler_765
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.595
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, Int, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/超好用WAN2.2-LightX2V-I2V_2010308124921569281.json, 视频生成/图生视频/首尾帧wan2.2  v1_2059895422222684162.json, 视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_765

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/超好用WAN2.2-LightX2V-I2V_2010308124921569281.json、视频生成/图生视频/首尾帧wan2.2  v1_2059895422222684162.json、视频生成/文生视频/1022Alan测-WAN2.2-LightX2V-I2V超强动态，高质量，高遵循度_1980811965771763713.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `WanImageToVideo` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `wanBlockSwap` —— 2/3 个有
- `DuckHideNode` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `WanFirstLastFrameToVideo` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 67%
