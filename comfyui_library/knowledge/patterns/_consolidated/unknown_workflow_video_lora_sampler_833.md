---
name: unknown_workflow_video_lora_sampler_833
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.547333
common_nodes: [CLIPLoader, CLIPTextEncode, GetNode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/让动漫人物跳江南Style骑马舞_1956547249952182274.json, 视频生成/图生视频/【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json, 视频生成/图生视频/一键生成超顶AI动漫视频！WAN2.2大模型太强了！_1951120660623990785.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_833

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/让动漫人物跳江南Style骑马舞_1956547249952182274.json、视频生成/图生视频/【gen全能视频Si】wan2.2-funcontrol让动漫人物跳舞_1961412963351597058.json、视频生成/图生视频/一键生成超顶AI动漫视频！WAN2.2大模型太强了！_1951120660623990785.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/3 个有
- `GetImageRangeFromBatch` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `RMBG` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `Wan22FunControlToVideo` —— 2/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有
- `wanBlockSwap` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 10 | 3 | 53% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 10，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
