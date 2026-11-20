---
name: unknown_workflow_video_upscale_clip
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.685667
common_nodes: [CLIPTextEncode, CR Upscale Image, Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PathchSageAttentionKJ, PreviewImage, SetNode, ShowText|pysssss, StringFunction|pysssss, VAEDecodeTiled, VHS_VideoCombine, WanVideoVACEStartToEndFrame, easy anythingIndexSwitch, easy int, easy positive, easy seed]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json, 平台全量/视频-动作迁移-wan2.2vace-官方_1973077709247131649.json, 视频生成/图生视频/Wan2.2-官方高质量【图生视频】+扩写提示词+HPS+MPS+FullDynamic_1975438275764686849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_clip

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json、平台全量/视频-动作迁移-wan2.2vace-官方_1973077709247131649.json、视频生成/图生视频/Wan2.2-官方高质量【图生视频】+扩写提示词+HPS+MPS+FullDynamic_1975438275764686849.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Upscale Image`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `CM_IntToFloat` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `TrimVideoLatent` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `VHS_VideoInfoLoaded` —— 2/3 个有
- `WanMoeKSampler` —— 2/3 个有
- `WanVaceToVideo` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Float` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `QwenLoader` —— 1/3 个有
- `WanImageToVideo` —— 1/3 个有
- `WanVideoPromptExtender` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 20 | 1 - 20 | 3 | 34% |
| 采样算法 | 1.25 | - | 2 | 80% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | sa_solver | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 20，观测区间 1 - 20，3 个样本，取值分散，一致性仅 34%
- 采样算法 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
