---
name: unknown_workflow_video_sampler_clip_141
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.45075
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), INTConstant, Int, ModelPatchTorchSettings, PathchSageAttentionKJ, RIFE VFI, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, wanBlockSwap]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2（t2v）+千问VL反推+音效_2002494004426076161.json, 图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json, 图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json, 视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Wan2.2（t2v）+千问VL反推+音效_2002494004426076161.json、图片生成/文生图/Work-Fisher_Wan2.2_Smooth Mix T2V_1979072068958457857.json、图片生成/文生图/文生视频Smootht2v+Qwen3VL反推+_2002512116349300738.json、视频生成/文生视频/Wan2.2+Qwen3VL+Foley模拟多模态全自动-文字-视频-声音_1987092853765640193.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 4 个 workflow 都包含：
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
- `WanImageToVideo`
- `WanMoeKSampler`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `UnetLoaderGGUF` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Any To Any` —— 2/4 个有
- `HunyuanVideoFoley` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `MultiplePathsInput` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `VHS_SelectFilename` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `easy float` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，4 个样本，一致性 100%
