---
name: unknown_workflow_video_lora_sampler_654
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.78
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfySwitchNode, ConditioningZeroOut, Fast Muter (rgthree), ImageCompositeMasked, ImageResizeKJv2, ImageScale, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMask, UNETLoader, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanContextWindowsManual, WanSCAILToVideo, easy convertAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/15.Scail2 多参考图+长视频+动作迁移+人物替换（不开火车）_2083566329239523330.json, 平台全量/15.Scail2 多参考图+长视频（不开火车）_2083834950012465153.json, 视频生成/图生视频/Scail2 官流多参考图+长视频（不开火车）_2074430549225205762.json, 视频生成/图生视频/动作迁移Scail2+多参考图+长视频wan2.1，_2077384295194390530.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_654

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/15.Scail2 多参考图+长视频+动作迁移+人物替换（不开火车）_2083566329239523330.json、平台全量/15.Scail2 多参考图+长视频（不开火车）_2083834950012465153.json、视频生成/图生视频/Scail2 官流多参考图+长视频（不开火车）_2074430549225205762.json、视频生成/图生视频/动作迁移Scail2+多参考图+长视频wan2.1，_2077384295194390530.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `Fast Muter (rgthree)`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `ImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanContextWindowsManual`
- `WanSCAILToVideo`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Label (rgthree)` —— 2/4 个有
- `ComfyMathExpression` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `SAM3_TrackPreview` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
- 高发问题（4/4 个样本）：发现KSampler但没有VAEDecode
