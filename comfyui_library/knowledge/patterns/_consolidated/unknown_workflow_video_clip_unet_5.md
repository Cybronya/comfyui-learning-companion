---
name: unknown_workflow_video_clip_unet_5
type: Unknown Workflow
frequency: 13
level: weak
coverage: 0.943615
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json, 视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json, 视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json, 视频生成/图生视频/Remix_i2v_v2.1图生视频工作流_2067237434458468353.json, 视频生成/图生视频/Remix超丝滑图生视频动态模型-官方工作流_1986706185669832705.json, 视频生成/图生视频/Remix超丝滑图生视频动态模型-官方工作流_2029757199156776962.json, 视频生成/图生视频/SmoothMix-V2.0首尾帧视频生成_2010689825397018625.json, 视频生成/图生视频/WH-AI-Studio-Wan2.2首尾帧加速完美版_2015621042139566081.json, 视频生成/图生视频/WH-AI-Studio-Wan2.2首帧-中间帧-尾帧（加速标准版首中尾帧图生视频）_2022240074083082242.json, 视频生成/图生视频/WH-AI-Studio（短剧必备）指定人物从指定场景出现（图生视频-加速完美版）（人物一致性）_2022215823229718529.json, 视频生成/图生视频/🐳wan2.2 首尾帧 极速臻享版 🦋【官方模型】_1952542983688261634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json、视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json、视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 12/13 个有
- `ModelSamplingSD3` —— 12/13 个有
- `LoraLoaderModelOnly` —— 8/13 个有
- `WanImageToVideo` —— 8/13 个有
- `CLIPVisionEncode` —— 7/13 个有
- `CLIPVisionLoader` —— 7/13 个有
- `PathchSageAttentionKJ` —— 7/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/13 个有
- `ImageResizeKJv2` —— 5/13 个有
- `SimpleMath+` —— 5/13 个有
- `CR Text` —— 4/13 个有
- `ImpactInt` —— 4/13 个有
- `WanFirstLastFrameToVideo` —— 4/13 个有
- `WanVideoNAG` —— 4/13 个有
- `ImageResizeKJ` —— 3/13 个有
- `ModelPatchTorchSettings` —— 3/13 个有
- `GetImageRangeFromBatch` —— 1/13 个有
- `GetImageSizeAndCount` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `ImageConcanate` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/13 个有
- `WanMoeKSampler` —— 1/13 个有
- `easy imageRemBg` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 54% |
| Prompt 约束强度(CFG) | 8 | 4 - 20 | 13 | 51% |
| 采样算法 | 1 | 1 - 3.5 | 13 | 44% |
| 调度器 | euler | - | 13 | 69% |
| 重绘幅度 | simple | - | 13 | 92% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 54%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 20，13 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，13 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，13 个样本，一致性 69%
- 重绘幅度 最常用 simple，13 个样本，一致性 92%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
