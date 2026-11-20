---
name: unknown_workflow_video_lora_sampler_676
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.93975
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PatchModelPatcherOrder, PreviewImage, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/VACE原生参考编辑(CausVid与AccVideo10步对比)_1928038128831840258.json, 视频生成/图生视频/单图参考-Wan2.1-VACE-Native_1924839944982831106.json, 视频生成/图生视频/参考编辑-Wan2.1-VACE-Native_1924845197476175874.json, 视频生成/图生视频/双图参考-Wan2.1-VACE-Native_1924845161095098369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_676

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/VACE原生参考编辑(CausVid与AccVideo10步对比)_1928038128831840258.json、视频生成/图生视频/单图参考-Wan2.1-VACE-Native_1924839944982831106.json、视频生成/图生视频/参考编辑-Wan2.1-VACE-Native_1924845197476175874.json、视频生成/图生视频/双图参考-Wan2.1-VACE-Native_1924845161095098369.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PreviewImage`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 3/4 个有
- `LayerMask: LoadFlorence2Model` —— 3/4 个有
- `LayerMask: ObjectDetectorFL2` —— 3/4 个有
- `LayerMask: SAM2Ultra` —— 3/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `InpaintPreprocessor` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `Image Blank` —— 1/4 个有
- `ImageCompositeMasked` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `InspyrenetRembg` —— 1/4 个有
- `easy ifElse` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 5 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
