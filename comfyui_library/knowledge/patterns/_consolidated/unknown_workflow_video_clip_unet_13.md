---
name: unknown_workflow_video_clip_unet_13
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9662
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Bypasser (rgthree), ImageResizeKJv2, ImpactInt, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json, 视频生成/图生视频/Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json, 视频生成/图生视频/Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json, 视频生成/图生视频/mj绝美风景短视频复刻首尾帧Wan2.2-Smooth Mix_2004053514764599297.json, 视频生成/图生视频/图生视频高动态 环无线时长版_1988425926365110274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2-SM无限时循环-高清动态图转视频_1987894798759735297.json、视频生成/图生视频/Wan2.2 SMOOTH MIX-单人物参考+自动运镜+长镜头生成（30秒）_1981343312810598402.json、视频生成/图生视频/Wan2.2图生视频高动态  FOR循环无线时长版_1981307265980555265.json、视频生成/图生视频/mj绝美风景短视频复刻首尾帧Wan2.2-Smooth Mix_2004053514764599297.json、视频生成/图生视频/图生视频高动态 环无线时长版_1988425926365110274.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Bypasser (rgthree)`
- `ImageResizeKJv2`
- `ImpactInt`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `MathExpression|pysssss` —— 4/5 个有
- `RIFE VFI` —— 4/5 个有
- `String Literal` —— 4/5 个有
- `Text Load Line From File` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `WanMoeKSampler` —— 4/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `WanFirstLastFrameToVideo` —— 1/5 个有
- `easy imageIndexSwitch` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | 1 | 1 - 1 | 4 | 100% |
| 重绘幅度 | euler_ancestral | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，5 个样本，一致性 80%
