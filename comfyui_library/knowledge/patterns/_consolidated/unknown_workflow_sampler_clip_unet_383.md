---
name: unknown_workflow_sampler_clip_unet_383
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86875
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxResolutionNode, JjkText, KSamplerSelect, Label (rgthree), LoadImage, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/品牌创意灵感_1888079162437951490.json, 平台全量/幸运IP过新年_1879814938511503362.json, 平台全量/毛绒玩具设计手稿_1879469214250557441.json, 平台全量/野兽派波普风景绘画_1869660766063202305.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_383

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/品牌创意灵感_1888079162437951490.json、平台全量/幸运IP过新年_1879814938511503362.json、平台全量/毛绒玩具设计手稿_1879469214250557441.json、平台全量/野兽派波普风景绘画_1869660766063202305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxResolutionNode`
- `JjkText`
- `KSamplerSelect`
- `Label (rgthree)`
- `LoadImage`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `TextCombinerTwo` —— 3/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `StyleModelLoader` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CLIPVisionEncode` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `StyleModelApplySimple` —— 1/4 个有
- `TextCombinerSix` —— 1/4 个有
- `VAEEncode` —— 1/4 个有
- `YC_LG_Redux` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageIndexSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 4 | 75% |
| 高度 | 1280 | 512 - 1280 | 4 | 69% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，4 个样本
- 高度 中位数 1280，观测区间 512 - 1280，4 个样本
