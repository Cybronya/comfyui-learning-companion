---
name: text_to_image_sampler_clip_checkpoint
type: Text To Image
frequency: 32
level: moderate
coverage: 0.893062
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_sdxl_simple.json, comfyui-workflow-templates-json/sdxl_revision_text_prompts.json, sd1.5/basic.json, 图片生成/文生图/1951180182470242305.json, 图片生成/文生图/1958497485645836289.json, 图片生成/文生图/1961283334359990274.json, 图片生成/文生图/1962370527010623489.json, 图片生成/文生图/1979111789180915714.json, 图片生成/文生图/1979377865538048002.json, 图片生成/文生图/1979390293403406337.json, 图片生成/文生图/1979445307241041922.json, 图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json, 图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json, 图片生成/文生图/SDLX1.0工作流_2065797462270504962.json, 图片生成/文生图/SDXL 国潮商业海报生成器_2069501911832817666.json, 图片生成/文生图/SDXL基础文生图工作流_2070416088365621250.json, 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json, 图片生成/文生图/【遇见AI】SD1.5文生图基础工作流_2011308014015352833.json, 图片生成/文生图/动漫二次云_2100884264383504386.json, 图片生成/文生图/基础文生图_2013163381582209026.json, 图片生成/文生图/夜色里的新中式建筑_2063975026935820290.json, 图片生成/文生图/文生图工作流+自选模型+全节点注释_2084250496327577602.json, 图片生成/文生图/漫画风古城街巷黄昏_2068266760830279682.json, 图片生成/文生图/男生酷帅动漫风 _ 高清头像壁纸生成器_2079536945205698562.json, 图片生成/文生图/第一章第三节图片猫咪生成0.3  0.61  1.0降噪_2060292921122975745.json, 图片生成/文生图/筑梦文生图_2063566740520521730.json, 图片生成/文生图/精致漫画风_2101660424197468161.json, 图片生成/文生图/自习时光_2063970318389174274.json, 图片生成/文生图/视频跟练_2106961244719767554.json, 图片生成/文生图/赛博朋克3D渲染风格_2071049568514564098.json, 图片生成/文生图/黑裙哥特少女_2096102392679976961.json, 数字人/数字人/酒吧美男_2089335688880807938.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 32 个 workflow 归纳得出（comfyui-workflow-templates-json/image_sdxl_simple.json、comfyui-workflow-templates-json/sdxl_revision_text_prompts.json、sd1.5/basic.json、图片生成/文生图/1951180182470242305.json、图片生成/文生图/1958497485645836289.json…）

- **类型**：Text To Image
- **样本数**：32
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 32 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/32 个有
- `CLIPVisionEncode` —— 1/32 个有
- `CLIPVisionLoader` —— 1/32 个有
- `unCLIPConditioning` —— 1/32 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 4 - 60 | 32 | 56% |
| Prompt 约束强度(CFG) | 7 | 1 - 8 | 32 | 64% |
| 采样算法 | euler | - | 32 | 53% |
| 调度器 | karras | - | 32 | 41% |
| 重绘幅度 | 1 | 0.9 - 1 | 32 | 98% |
| 宽度 | 768 | 480 - 1920 | 32 | 65% |
| 高度 | 1024 | 512 - 1920 | 32 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/32 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 4 - 60，32 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1 - 8，32 个样本
- 采样算法 最常用 euler，32 个样本，一致性 53%
- 调度器 最常用 karras，32 个样本，一致性 41%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，32 个样本，取值集中（一致性 98%）
- 宽度 中位数 768，观测区间 480 - 1920，32 个样本
- 高度 中位数 1024，观测区间 512 - 1920，32 个样本
