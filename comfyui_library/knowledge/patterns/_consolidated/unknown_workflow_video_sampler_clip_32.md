---
name: unknown_workflow_video_sampler_clip_32
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.978714
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json, 视频生成/图生视频/87time WAN 图生视频_1913510854523060225.json, 视频生成/图生视频/FusioniX图生视频_1947317037666291713.json, 视频生成/图生视频/UNET加载器跑wan2.1视频_1935624782786527233.json, 视频生成/图生视频/WAN2.1图生视频_1902195474282258433.json, 视频生成/图生视频/Wan2.1 360度旋转_1938538805421105153.json, 视频生成/图生视频/Wan2.1 万相 飞天特效_1910876944500752386.json, 视频生成/图生视频/Wan2.1 万相360度万物旋转（超快）_1910598046382784514.json, 视频生成/图生视频/Wan2.1 万相图生视频_1902233258837303298.json, 视频生成/图生视频/Wan2.1 图生视频+Lora 工作流_1942457845642366977.json, 视频生成/图生视频/Wan2.1 图生视频+Lora 工作流【AI小王子】_1902895670603460609.json, 视频生成/图生视频/Wan2.1 图生视频_1911283580138418178.json, 视频生成/图生视频/Wan2.1 通义万相 捏捏特效 捏扁特效_1911587726854975489.json, 视频生成/图生视频/万相wan2.1 图生视频 ComfyUI org 官方流  B站 楚门的AI世界_1894951787738824705.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/万相wan2.1极致图生视频ComfyUI_1906877379761905665.json、视频生成/图生视频/87time WAN 图生视频_1913510854523060225.json、视频生成/图生视频/FusioniX图生视频_1947317037666291713.json、视频生成/图生视频/UNET加载器跑wan2.1视频_1935624782786527233.json、视频生成/图生视频/WAN2.1图生视频_1902195474282258433.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 12/14 个有
- `UNETLoader` —— 10/14 个有
- `WanVideoTeaCacheKJ` —— 9/14 个有
- `LoraLoaderModelOnly` —— 6/14 个有
- `WanVideoEnhanceAVideoKJ` —— 6/14 个有
- `Int` —— 4/14 个有
- `UnetLoaderGGUF` —— 4/14 个有
- `TextInput_` —— 2/14 个有
- `ImageUpscaleWithModel` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `ModelSamplingSD3` —— 1/14 个有
- `UpscaleModelLoader` —— 1/14 个有
- `WanVideoModelLoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 14 | 87% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 14 | 75% |
| 采样算法 | uni_pc | - | 14 | 93% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，14 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，14 个样本
- 采样算法 最常用 uni_pc，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
