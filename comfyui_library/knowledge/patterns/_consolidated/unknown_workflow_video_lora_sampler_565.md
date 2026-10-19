---
name: unknown_workflow_video_lora_sampler_565
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.796667
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, SplitSigmas, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, easy cleanGpuUsed]
members: [图片生成/文生图/1952356133568745474.json, 图片生成/文生图/1954793772753182722.json, 图片生成/文生图/1973082031938736129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_565

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1952356133568745474.json、图片生成/文生图/1954793772753182722.json、图片生成/文生图/1973082031938736129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1ExtraOptions` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1152 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: JoyCaptionBeta1、LayerUtility: JoyCaptionBeta1ExtraOptions、LayerUtility: LoadJoyCaptionBeta1Model、easy cleanGpuUsed
