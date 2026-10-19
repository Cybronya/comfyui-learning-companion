---
name: unknown_workflow_video_lora_sampler_164
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.882545
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler]
problems: []
missing: []
members: [视频生成/图生视频/2055131714812432386.json, 视频生成/图生视频/1982433270455508994.json, 视频生成/图生视频/2017048287710289922.json, 视频生成/图生视频/2063160454893096961.json, 视频生成/图生视频/1980667060764233730.json, 视频生成/图生视频/2010604596271521794.json, 视频生成/图生视频/2029383179194339329.json, 视频生成/图生视频/2056287070284505090.json, 视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json, 视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json, 视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_164

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2055131714812432386.json、视频生成/图生视频/1982433270455508994.json、视频生成/图生视频/2017048287710289922.json、视频生成/图生视频/2063160454893096961.json、视频生成/图生视频/1980667060764233730.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`

**可变部分**（部分 workflow 才有）：
- `WanFirstLastFrameToVideo` —— 10/11 个有
- `CLIPVisionEncode` —— 9/11 个有
- `CLIPVisionLoader` —— 9/11 个有
- `WanImageToVideo` —— 8/11 个有
- `DownloadAndLoadGIMMVFIModel` —— 7/11 个有
- `EmptyHunyuanLatentVideo` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 7/11 个有
- `GIMMVFI_interpolate` —— 7/11 个有
- `wanBlockSwap` —— 7/11 个有
- `ImageResizeKJv2` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `FL_RIFE` —— 4/11 个有
- `easy int` —— 4/11 个有
- `Fast Groups Muter (rgthree)` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 6 | 3 - 8 | 11 | 81% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | 1 | 1 - 1 | 11 | 100% |
| 重绘幅度 | euler | - | 11 | 64% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 6，观测区间 3 - 8，11 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，11 个样本，一致性 64%
