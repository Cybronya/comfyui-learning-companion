---
name: unknown_workflow_video_clip_unet_12
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.439286
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, Int, ModelPatchTorchSettings, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, wanBlockSwap]
problems: []
missing: [RIFE VFI, easy cleanGpuUsed]
members: [图片生成/文生图/1979072068958457857.json, 图片生成/文生图/Wan2.2（t2v）+千问VL反推+音效_2002494004426076161.json, 图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json, 视频生成/图生视频/2076490092809637889.json, 视频生成/图生视频/1987069561856004097.json, 视频生成/图生视频/1987091319136956418.json, 视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1979072068958457857.json、图片生成/文生图/Wan2.2（t2v）+千问VL反推+音效_2002494004426076161.json、图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json、视频生成/图生视频/2076490092809637889.json、视频生成/图生视频/1987069561856004097.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Int`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `WanImageToVideo` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `Any To Any` —— 5/7 个有
- `HunyuanVideoFoley` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `MultiplePathsInput` —— 5/7 个有
- `Qwen3_VQA` —— 5/7 个有
- `VHS_SelectFilename` —— 5/7 个有
- `easy float` —— 5/7 个有
- `WanMoeKSampler` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `KSamplerAdvanced` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `ModelSamplingSD3` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `UnetLoaderGGUF` —— 3/7 个有
- `LoadImage` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `AILab_QwenVL` —— 1/7 个有
- `ImageLoader` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 7 | 81% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 7 | 57% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，7 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，7 个样本，一致性 57%
- 这些节点还没有知识卡，系统对它们的理解有限：RIFE VFI、easy cleanGpuUsed
