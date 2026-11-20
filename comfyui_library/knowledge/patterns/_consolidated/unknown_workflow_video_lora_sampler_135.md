---
name: unknown_workflow_video_lora_sampler_135
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.879923
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler]
problems: []
missing: []
members: [图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json, 视频生成/图生视频/WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json, 视频生成/图生视频/Wan2.2 light I2V 4步图文生视频&首尾帧v1_1982433270455508994.json, 视频生成/图生视频/Wan2.2 图文生视频&首尾帧_2017048287710289922.json, 视频生成/图生视频/Wan2.2 图生视频 团子专用_2063160454893096961.json, 视频生成/图生视频/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980667060764233730.json, 视频生成/图生视频/首尾帧_图生视频 真实感还原_2010604596271521794.json, 视频生成/图生视频/首尾帧_图生视频漫剧生成器_2029383179194339329.json, 视频生成/图生视频/首尾帧_图生视频漫剧生成器_2056287070284505090.json, 视频生成/文生视频/1022Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1980828355211776002.json, 视频生成/文生视频/1023Alan自用-Wan2.2 图文生视频&首尾帧3合1加速版v1_1981047822306918402.json, 视频生成/文生视频/Wan2.2 首尾帧3合1加速版v1_2066350014036791297.json, 视频生成/文生视频/首尾帧_图生视频LightX2V快速流_2010388092464664578.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_135

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/YZ金鱼-Wan2.2 图文生视频&首尾帧3合1加速版v1_2060019371350777858.json、视频生成/图生视频/WAN2.2极致细节图生视频工作流（首尾帧）_2055131714812432386.json、视频生成/图生视频/Wan2.2 light I2V 4步图文生视频&首尾帧v1_1982433270455508994.json、视频生成/图生视频/Wan2.2 图文生视频&首尾帧_2017048287710289922.json、视频生成/图生视频/Wan2.2 图生视频 团子专用_2063160454893096961.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
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
- `WanFirstLastFrameToVideo` —— 11/13 个有
- `CLIPVisionEncode` —— 10/13 个有
- `CLIPVisionLoader` —— 10/13 个有
- `WanImageToVideo` —— 9/13 个有
- `DownloadAndLoadGIMMVFIModel` —— 8/13 个有
- `EmptyHunyuanLatentVideo` —— 8/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `GIMMVFI_interpolate` —— 8/13 个有
- `wanBlockSwap` —— 8/13 个有
- `ImageResizeKJv2` —— 7/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `FL_RIFE` —— 5/13 个有
- `easy int` —— 4/13 个有
- `Fast Groups Muter (rgthree)` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 92% |
| Prompt 约束强度(CFG) | 6 | 3 - 8 | 13 | 82% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | 1 | 1 - 1 | 13 | 100% |
| 重绘幅度 | euler | - | 13 | 62% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 92%
- Prompt 约束强度(CFG) 中位数 6，观测区间 3 - 8，13 个样本，取值集中（一致性 82%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，13 个样本，一致性 62%
