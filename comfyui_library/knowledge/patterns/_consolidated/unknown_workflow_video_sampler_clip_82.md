---
name: unknown_workflow_video_sampler_clip_82
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.80925
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Groups Bypasser (rgthree), INTConstant, Int, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频_2014967936171118594.json, 视频生成/图生视频/Wan2.2_Smooth-Mix-I2V-常规图生视频和首尾帧生视频_1998270569793617921.json, 视频生成/图生视频/Wan2.2_Smooth_I2V_1978100410332372994.json, 视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json, 视频生成/图生视频/painterI2V_Smooth-Mix-I2V-动态强度可调版_1991393474855677954.json, 视频生成/图生视频/升帧率版！视频更流畅！SmoothMix图生视频工作流_2041940547862011906.json, 视频生成/图生视频/图生视频三合一_1989202915321589761.json, 视频生成/图生视频/首尾帧_图生视频四合一_1992859603580899330.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2_Smooth Mix I2V图生视频_2014967936171118594.json、视频生成/图生视频/Wan2.2_Smooth-Mix-I2V-常规图生视频和首尾帧生视频_1998270569793617921.json、视频生成/图生视频/Wan2.2_Smooth_I2V_1978100410332372994.json、视频生成/图生视频/Work-Fisher_Wan2.2_Smooth Mix I2V_1977733586520526849.json、视频生成/图生视频/painterI2V_Smooth-Mix-I2V-动态强度可调版_1991393474855677954.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Int`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 7/8 个有
- `RIFE VFI` —— 7/8 个有
- `WanImageToVideo` —— 6/8 个有
- `wanBlockSwap` —— 6/8 个有
- `DF_Integer` —— 5/8 个有
- `SimpleMath+` —— 5/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `FL_RIFE` —— 2/8 个有
- `KSamplerAdvanced` —— 2/8 个有
- `LoraLoaderModelOnly` —— 2/8 个有
- `ModelSamplingSD3` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ImageLoader` —— 1/8 个有
- `PainterI2V` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 50% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 8 | 79% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | 1 | 1 - 1 | 6 | 100% |
| 重绘幅度 | euler_ancestral | - | 8 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，8 个样本，一致性 75%
