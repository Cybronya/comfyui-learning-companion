---
name: unknown_workflow_video_lora_sampler_82
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.902333
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, AudioInfo, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Evaluate Integers, ImageBatch, ImageFromBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, ModelPatchLoader, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanInfiniteTalkToVideo, easy forLoopEnd, easy forLoopStart, easy int, easy mathInt]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/InfiniteTalk-ComfyUI官版自循环_2019259304406159362.json, 数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json, 数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化_2032746856781979650.json, 数字人/数字人/InfiniteTalk-ComfyUI官版自循环版（质量不劣化）_2018972622758879233.json, 数字人/数字人/InfiniteTalk-anycom_2058890249543176193.json, 数字人/数字人/InfiniteTalk-官版双人数字人自循环版（质量不劣化）_2019674131742068737.json, 数字人/数字人/InfiniteTalk-数字人官方自循环_2019377383660326913.json, 数字人/数字人/InfiniteTalki官流 长视频无衰减自循环_2019342054777688065.json, 数字人/数字人/InfiniteTalk数字人MV_2076641541761880066.json, 数字人/数字人/新InfiniteTalk-Comfyui官方魔改多图无限长视频数字人_2028667164265291777.json, 视频生成/图生视频/InfiniteTalk- 高质量图生视频 数字人MV 超长时间视频生成_2025770017006030849.json, 视频生成/图生视频/InfiniteTalk-ComfyUI官版数字人MV_2019621453360013313.json, 视频生成/图生视频/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化 +全节点注释_2056921656811147266.json, 视频生成/图生视频/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化_2024713111399309314.json, 视频生成/图生视频/InfiniteTalk-ComfyUI官版自循环版（质量不劣化）_2019616198597550082.json, 视频生成/图生视频/InfiniteTalk-官版数字人MV_多图自动连帧直出_2019582542961188866.json, 视频生成/图生视频/[🛫书墨]infinitetalk(官方单图无限for循环自动计算版)_2018961391968849921.json, 视频生成/图生视频/[🛫书墨]infinitetalk官方无限多图平均帧for循环版_2019080494813552642.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_82

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（数字人/数字人/InfiniteTalk-ComfyUI官版自循环_2019259304406159362.json、数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化-yun自用_2026705165088202753.json、数字人/数字人/InfiniteTalk-ComfyUI官版自循环版+3分钟高速平衡优化_2032746856781979650.json、数字人/数字人/InfiniteTalk-ComfyUI官版自循环版（质量不劣化）_2018972622758879233.json、数字人/数字人/InfiniteTalk-anycom_2058890249543176193.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `AudioInfo`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Evaluate Integers`
- `ImageBatch`
- `ImageFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `ModelPatchLoader`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanInfiniteTalkToVideo`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy int`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `AudioTrim` —— 16/18 个有
- `KSampler` —— 16/18 个有
- `Text Multiline` —— 15/18 个有
- `PreviewAudio` —— 12/18 个有
- `easy showAnything` —— 12/18 个有
- `Fast Bypasser (rgthree)` —— 8/18 个有
- `Mute / Bypass Repeater (rgthree)` —— 8/18 个有
- `GetImageSize` —— 5/18 个有
- `JWFloat` —— 5/18 个有
- `ImageBatchMulti` —— 4/18 个有
- `MathExpression|pysssss` —— 4/18 个有
- `PurgeVRAM_UTK` —— 3/18 个有
- `RHHiddenNodes` —— 3/18 个有
- `Any Switch (rgthree)` —— 2/18 个有
- `BasicScheduler` —— 2/18 个有
- `CFGGuider` —— 2/18 个有
- `Fast Groups Muter (rgthree)` —— 2/18 个有
- `KSamplerSelect` —— 2/18 个有
- `RandomNoise` —— 2/18 个有
- `SamplerCustomAdvanced` —— 2/18 个有
- `AudioConcat` —— 1/18 个有
- `AudioCrop` —— 1/18 个有
- `AudioMerge` —— 1/18 个有
- `BatchCount+` —— 1/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有
- `Float` —— 1/18 个有
- `Image Batch` —— 1/18 个有
- `ImpactStringSelector` —— 1/18 个有
- `Int` —— 1/18 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/18 个有
- `PreviewImage` —— 1/18 个有
- `PrimitiveStringMultiline` —— 1/18 个有
- `ProcessString` —— 1/18 个有
- `ShowText|pysssss` —— 1/18 个有
- `easy convertAnything` —— 1/18 个有
- `easy ifElse` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 3 - 4 | 16 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | normal | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 32/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 3 - 4，16 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 normal，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（32/18 个样本）：Steps较低可能导致细节不足
