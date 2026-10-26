---
name: text_to_image_sampler_clip_unet_52
type: Text To Image
frequency: 11
level: strong
coverage: 0.888545
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Anima 动漫图生图_2057268821492330497.json, 图片生成/图生图/Anima一键反推动漫人物_2017853202951053313.json, 图片生成/图生图/Anima一键洗图生成动漫_2029386606406279169.json, 图片生成/图生图/Anima一键洗图转动漫（极速）_2029926543564218370.json, 图片生成/图生图/Anima图生图一键洗图生成动漫_2018241461094977538.json, 图片生成/图生图/Anima图生图一键洗图生成动漫_2028269065684393986.json, 图片生成/图生图/Anima图生图一键洗图生成动漫_2037006149911842817.json, 图片生成/图生图/Anima图生图一键洗图生成动漫_2037068489604730882.json, 图片生成/图生图/Anima图生图一键洗图生成动漫_2044291988693979138.json, 图片生成/图生图/Anima图生图一键洗图生成动漫图工作流_2050785288980582401.json, 图片生成/文生图/图生图生成动漫_2033813819365007361.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Anima 动漫图生图_2057268821492330497.json、图片生成/图生图/Anima一键反推动漫人物_2017853202951053313.json、图片生成/图生图/Anima一键洗图生成动漫_2029386606406279169.json、图片生成/图生图/Anima一键洗图转动漫（极速）_2029926543564218370.json、图片生成/图生图/Anima图生图一键洗图生成动漫_2018241461094977538.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 10/11 个有
- `ModelSamplingAuraFlow` —— 10/11 个有
- `ImageResizeKJv2` —— 9/11 个有
- `RH_LLMAPI_Pro_Node` —— 9/11 个有
- `ResizeLongestToNode` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `AILab_QwenVL` —— 1/11 个有
- `PrimitiveInt` —— 1/11 个有
- `RH_Captioner` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 30 - 40 | 11 | 91% |
| Prompt 约束强度(CFG) | 4 | 4 - 4.5 | 11 | 96% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 896 | 512 - 1920 | 11 | 66% |
| 高度 | 1152 | 512 - 1152 | 11 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 30 - 40，11 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4.5，11 个样本，取值集中（一致性 96%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1920，11 个样本
- 高度 中位数 1152，观测区间 512 - 1152，11 个样本，取值集中（一致性 83%）
