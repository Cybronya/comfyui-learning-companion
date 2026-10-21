---
name: unknown_workflow_video_sampler_clip_20
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.836235
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Int, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2049387851611119618.json, 视频生成/图生视频/2009138591993171970.json, 视频生成/图生视频/2049389424517058561.json, 视频生成/图生视频/2011360351337586690.json, 视频生成/图生视频/2014967936171118594.json, 视频生成/图生视频/2003656092246786049.json, 视频生成/图生视频/2012356718814040065.json, 视频生成/图生视频/2012366284465377282.json, 视频生成/图生视频/2008710367467278338.json, 视频生成/图生视频/1998270569793617921.json, 视频生成/图生视频/1978100410332372994.json, 视频生成/图生视频/1977733586520526849.json, 视频生成/图生视频/1991393474855677954.json, 视频生成/图生视频/2041940547862011906.json, 视频生成/图生视频/1989202915321589761.json, 视频生成/图生视频/1992859603580899330.json, 视频生成/图生视频/1978131739417665538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2049387851611119618.json、视频生成/图生视频/2009138591993171970.json、视频生成/图生视频/2049389424517058561.json、视频生成/图生视频/2011360351337586690.json、视频生成/图生视频/2014967936171118594.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
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
- `ImageResizeKJv2` —— 16/17 个有
- `Fast Groups Bypasser (rgthree)` —— 15/17 个有
- `INTConstant` —— 15/17 个有
- `RIFE VFI` —— 15/17 个有
- `wanBlockSwap` —— 15/17 个有
- `DF_Integer` —— 13/17 个有
- `SimpleMath+` —— 13/17 个有
- `WanImageToVideo` —— 12/17 个有
- `WanFirstLastFrameToVideo` —— 11/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/17 个有
- `FL_RIFE` —— 2/17 个有
- `KSamplerAdvanced` —— 2/17 个有
- `LoraLoaderModelOnly` —— 2/17 个有
- `ModelSamplingSD3` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `ImageLoader` —— 1/17 个有
- `PainterI2V` —— 1/17 个有
- `PlaySound|pysssss` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `Text` —— 1/17 个有
- `Textbox` —— 1/17 个有
- `easy int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 17 | 65% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 17 | 80% |
| 采样算法 | 1 | 1 - 1 | 17 | 100% |
| 调度器 | 1 | 1 - 1 | 15 | 100% |
| 重绘幅度 | euler_ancestral | - | 17 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，17 个样本，一致性 65%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，17 个样本
- 采样算法 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，17 个样本，一致性 88%
