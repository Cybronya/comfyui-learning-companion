---
name: unknown_workflow_video_lora_sampler_809
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.994333
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, INTConstant, ImageResizeKJ, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PatchModelPatcherOrder, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: []
missing: []
members: [平台全量/VACE-更精准的姿态调节-视频转绘_1932353856917635074.json, 平台全量/控制+参考(CausVid与AccVideo10步对比)_1928029684129513473.json, 视频生成/图生视频/控制+参考-Wan2.1-VACE-Native_1924845181453934593.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_809

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/VACE-更精准的姿态调节-视频转绘_1932353856917635074.json、平台全量/控制+参考(CausVid与AccVideo10步对比)_1928029684129513473.json、视频生成/图生视频/控制+参考-Wan2.1-VACE-Native_1924845181453934593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJ`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `MyOpenPoseNode` —— 1/3 个有
- `OpenposePreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
