---
name: unknown_workflow_video_clip_unet_3
type: Unknown Workflow
frequency: 14
level: weak
coverage: 0.865
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json, 视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json, 视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json, 视频生成/图生视频/Remix_i2v_v2.1图生视频工作流_2067237434458468353.json, 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2026835055515017218.json, 视频生成/图生视频/Smooth Mix i2V v2.0图生视频8步加速版_2056759291427778562.json, 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2026846377501790209.json, 视频生成/图生视频/Smooth Mix i2V v2.0首尾帧生视频8步加速版_2038172701340213249.json, 视频生成/图生视频/WAN2.2 图生视频 4步出图_2016945597965672449.json, 视频生成/图生视频/WAN2.2 图生视频-首帧参考版_2027809490925527041.json, 视频生成/图生视频/WAN2.2首尾帧_2021954787742326786.json, 视频生成/图生视频/smooth首尾帧图生视频工作流_2067255627071709185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json、视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json、视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 13/14 个有
- `ModelSamplingSD3` —— 13/14 个有
- `LoraLoaderModelOnly` —— 11/14 个有
- `WanImageToVideo` —— 10/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/14 个有
- `ImageResize+` —— 4/14 个有
- `WanFirstLastFrameToVideo` —— 4/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `WanMoeKSampler` —— 1/14 个有
- `WanVideoNAG` —— 1/14 个有
- `easy convertAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 14 | 57% |
| Prompt 约束强度(CFG) | 9 | 4 - 20 | 14 | 48% |
| 采样算法 | 1 | 1 - 3.5 | 14 | 45% |
| 调度器 | euler | - | 14 | 93% |
| 重绘幅度 | simple | - | 14 | 93% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，14 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 9，观测区间 4 - 20，14 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 1，观测区间 1 - 3.5，14 个样本，取值分散，一致性仅 45%
- 调度器 最常用 euler，14 个样本，一致性 93%
- 重绘幅度 最常用 simple，14 个样本，一致性 93%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
