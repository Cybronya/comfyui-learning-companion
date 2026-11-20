---
name: unknown_workflow_video_lora_sampler_105
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.870313
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/kone专属图生视频_2007088250229366786.json, 视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json, 视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json, 视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json, 视频生成/图生视频/wan2_2_子弹时间 极速版_1984472483812229122.json, 视频生成/图生视频/【图生视频】Wan2.2 14B LightX2V_1953391288357978113.json, 视频生成/图生视频/一键生成超顶AI动漫视频！WAN2.2大模型太强了！_1951120660623990785.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2053500201926705153.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2054607136101027841.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063711056727461890.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063712287315292162.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063714093613281281.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2063914082952114178.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2072973666828251138.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2 wan22_2083074284628566017.json, 视频生成/图生视频/首尾帧  多帧  视频生成 wan2.2_2048315037026099202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_105

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/kone专属图生视频_2007088250229366786.json、视频生成/图生视频/wan2.2 图生视频_2030667044726771713.json、视频生成/图生视频/wan2_2_14B_I2V _4步加速_1998388818095013889.json、视频生成/图生视频/wan2_2_14B_I2V图生视频加速工作流_1969634228759633922.json、视频生成/图生视频/wan2_2_子弹时间 极速版_1984472483812229122.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 15/16 个有
- `ModelPatchTorchSettings` —— 14/16 个有
- `UNETLoader` —— 11/16 个有
- `GetNode` —— 10/16 个有
- `INTConstant` —— 10/16 个有
- `SetNode` —— 10/16 个有
- `SimpleMath+` —— 9/16 个有
- `WanFirstMiddleLastFrameToVideo` —— 9/16 个有
- `WanImageToVideo` —— 7/16 个有
- `UnetLoaderGGUF` —— 5/16 个有
- `LayerUtility: PurgeVRAM` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `Label (rgthree)` —— 1/16 个有
- `MathExpression|pysssss` —— 1/16 个有
- `SaveImage` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 16 | 69% |
| Prompt 约束强度(CFG) | 6 | 4 - 10 | 16 | 76% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler | - | 16 | 94% |
| 重绘幅度 | simple | - | 16 | 56% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，16 个样本，一致性 69%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 10，16 个样本
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，16 个样本，一致性 94%
- 重绘幅度 最常用 simple，16 个样本，一致性 56%
