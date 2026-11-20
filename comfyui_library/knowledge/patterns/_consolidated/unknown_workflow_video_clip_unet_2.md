---
name: unknown_workflow_video_clip_unet_2
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.918889
common_nodes: [CLIPLoader, CLIPTextEncode, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json, 视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json, 视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json, 视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json, 视频生成/图生视频/Remix_i2v_v2.1图生视频工作流_2067237434458468353.json, 视频生成/图生视频/Remix超丝滑图生视频动态模型-官方工作流_1986706185669832705.json, 视频生成/图生视频/Remix超丝滑图生视频动态模型-官方工作流_2029757199156776962.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996401587960561665.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1954509798727413761.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1993525014328705026.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114564471111905282.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_2114671381353943042.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频加速版_1950026797163438082.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 图生视频（工作室自用）_2027632357276131329.json, 视频生成/图生视频/Wan2.2 14B+LightX2V超极速图生视频_1952642819863318529.json, 视频生成/图生视频/Wan2.2 Smooth高质量图生视频极速版_2033413176150204417.json, 视频生成/图生视频/wan2.2图生视频Smooth版_2039903476511150082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/0001-WAN2.2-基础图生视频_2051154615328092161.json、视频生成/图生视频/06wan2.2图生视频+全节点注释_2055499386683183105.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频_2076115967696003073.json、视频生成/图生视频/Aiwood wan2.2+2.1二阶图生视频，上传图片加入提示词，点击运行生成所需视频，高清好用！_2075475746235174913.json、视频生成/图生视频/Remix Wan2.2-i2V 6步极速版版-官方版_2018238424574070785.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 17/18 个有
- `ModelSamplingSD3` —— 17/18 个有
- `WanImageToVideo` —— 17/18 个有
- `LoraLoaderModelOnly` —— 13/18 个有
- `PathchSageAttentionKJ` —— 12/18 个有
- `LayerUtility: PurgeVRAM` —— 8/18 个有
- `JWInteger` —— 7/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/18 个有
- `CLIPVisionEncode` —— 4/18 个有
- `CLIPVisionLoader` —— 4/18 个有
- `ModelPatchTorchSettings` —— 3/18 个有
- `ImageResizeKJv2` —— 2/18 个有
- `Seed (rgthree)` —— 2/18 个有
- `easy cleanGpuUsed` —— 2/18 个有
- `CR Prompt Text` —— 1/18 个有
- `Float` —— 1/18 个有
- `ImageScaleBy` —— 1/18 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 1/18 个有
- `RunningHub Deepcleaner` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `Text` —— 1/18 个有
- `UnetLoaderGGUF` —— 1/18 个有
- `WanMoeKSampler` —— 1/18 个有
- `easy anythingIndexSwitch` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 78% |
| Prompt 约束强度(CFG) | 6 | 4 - 20 | 18 | 48% |
| 采样算法 | 1 | 1 - 3.5 | 18 | 50% |
| 调度器 | lcm | - | 18 | 44% |
| 重绘幅度 | simple | - | 18 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 78%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 20，18 个样本，取值分散，一致性仅 48%
- 采样算法 中位数 1，观测区间 1 - 3.5，18 个样本，取值分散，一致性仅 50%
- 调度器 最常用 lcm，18 个样本，一致性 44%
- 重绘幅度 最常用 simple，18 个样本，一致性 94%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
