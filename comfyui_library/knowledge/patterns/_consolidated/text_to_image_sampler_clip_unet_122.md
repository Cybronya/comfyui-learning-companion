---
name: text_to_image_sampler_clip_unet_122
type: Text To Image
frequency: 6
level: weak
coverage: 0.921833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json, 图片生成/文生图/Y-qwen_image_2512_workflow_2006635024417824770.json, 图片生成/文生图/Z-image-base文生图官方版_2018889742305202178.json, 图片生成/文生图/文字头像抽卡神器_自动生成_2084090261851955202.json, 图片生成/文生图/风格文字头像自动生成_2080232577151102978.json, 图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007665464629010433.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_122

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Worker Text2Image V1.1_1988431547948818433.json、图片生成/文生图/Y-qwen_image_2512_workflow_2006635024417824770.json、图片生成/文生图/Z-image-base文生图官方版_2018889742305202178.json、图片生成/文生图/文字头像抽卡神器_自动生成_2084090261851955202.json、图片生成/文生图/风格文字头像自动生成_2080232577151102978.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `LoraLoaderModelOnly` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 4/6 个有
- `DapaoImageRatioLimitNode` —— 3/6 个有
- `Seed (rgthree)` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `easy int` —— 3/6 个有
- `InversionDemoLazyIndexSwitch` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `QwenEditResolution` —— 1/6 个有
- `SDXL Resolutions (JPS)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 19.5 | 8 - 50 | 6 | 29% |
| Prompt 约束强度(CFG) | 1.3 | 1 - 4 | 6 | 41% |
| 采样算法 | res_multistep | - | 6 | 33% |
| 调度器 | simple | - | 6 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | 16 - 1088 | 6 | 43% |
| 高度 | 512 | 16 - 2080 | 6 | 16% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 19.5，观测区间 8 - 50，6 个样本，取值分散，一致性仅 29%
- Prompt 约束强度(CFG) 中位数 1.3，观测区间 1 - 4，6 个样本，取值分散，一致性仅 41%
- 采样算法 最常用 res_multistep，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 16 - 1088，6 个样本，取值分散，一致性仅 43%
- 高度 中位数 512，观测区间 16 - 2080，6 个样本，取值分散，一致性仅 16%
- 高发问题（3/6 个样本）：Steps较低可能导致细节不足
