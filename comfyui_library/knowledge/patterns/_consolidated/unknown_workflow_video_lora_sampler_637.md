---
name: unknown_workflow_video_lora_sampler_637
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.901
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, DisableNoise, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RH_Captioner, RandomNoise, SamplerCustomAdvanced, SaveImage, SplitSigmas, UNETLoader, VAEDecode, VAELoader, WanVideoNAG]
problems: []
missing: []
members: [图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json, 图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json, 图片生成/文生图/Wan2.2反推文生图_1973082031938736129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_637

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/纯种WAN2.2以图洗图(文字版Redux)_1953709934967967746.json、图片生成/图生图/纯种WAN2.2洗图(秒杀Krea)_1938145100054577154.json、图片生成/文生图/Wan2.2反推文生图_1973082031938736129.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RH_Captioner`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `PrimitiveFloat` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageMirror` —— 1/3 个有
- `ImageResize` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1152 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
