---
name: unknown_workflow_video_lora_clip_14
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, GetImageSize+, INTConstant, ImagePadKJ, ImageResizeKJ, LoraLoaderModelOnly, MaskToImage, ModelSamplingSD3, String Literal, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/VACE原生视频扩展(CausVid与AccVideo10步对比)_1928043854203600897.json, 平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json, 平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_14

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE原生视频扩展(CausVid与AccVideo10步对比)_1928043854203600897.json、平台全量/Wan2.2-VACE-视频扩展_1950458342490685442.json、平台全量/视频扩展-Wan2.1-VACE-Native_1925061061618429953.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `INTConstant`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelSamplingSD3`
- `String Literal`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 2/3 个有
- `PatchModelPatcherOrder` —— 2/3 个有
- `TorchCompileModelWanVideo` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `JWImageExtractFromBatch` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MiniCPM_VQA` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有
- `easy int` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 4 | 1 - 10 | 3 | 25% |
| 采样算法 | uni_pc | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 10，3 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 uni_pc，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
