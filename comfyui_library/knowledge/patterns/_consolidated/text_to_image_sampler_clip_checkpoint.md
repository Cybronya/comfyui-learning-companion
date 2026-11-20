---
name: text_to_image_sampler_clip_checkpoint
type: Text To Image
frequency: 36
level: moderate
coverage: 0.899194
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_sdxl_simple.json, comfyui-workflow-templates-json/sdxl_revision_text_prompts.json, sd1.5/basic.json, 图片生成/图生图/test_2060392964412764161.json, 图片生成/图生图/文生图基础款_1980202895117291522.json, 图片生成/文生图/Mymang-Qwen 2509 AIO文生图_1977361796124286978.json, 图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json, 图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json, 图片生成/文生图/SD_1971226483622658049.json, 图片生成/文生图/XL文生图基础款_1946346552236339202.json, 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json, 图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json, 图片生成/文生图/别墅庭院风_2063986622978420738.json, 图片生成/文生图/动漫_2070124661043716097.json, 图片生成/文生图/动漫二次云_2100884264383504386.json, 图片生成/文生图/动漫女孩_2101663777623207938.json, 图片生成/文生图/动漫美少女_2072470520804761601.json, 图片生成/文生图/卡通3D形象生成器_1916402793215623169.json, 图片生成/文生图/咖啡馆漫画风_2101655459567591426.json, 图片生成/文生图/场景生成_2039074931979325441.json, 图片生成/文生图/基础工作流_1914506513556172801.json, 图片生成/文生图/基础文生图工作流+全节点注释_2055473668087656449.json, 图片生成/文生图/文生图-极速-3D卡通_2101863055092178945.json, 图片生成/文生图/文生图基础款-v1_1980214445693689857.json, 图片生成/文生图/文生图基础款1_1851544019800313857.json, 图片生成/文生图/文生图基础款_1818200162132209665.json, 图片生成/文生图/文生图基础款_1830501484281688065.json, 图片生成/文生图/文生图基础款_1851451030012841985.json, 图片生成/文生图/文生图基础款_1902358353320816641.json, 图片生成/文生图/文生图基础款_1907783762778664961.json, 图片生成/文生图/文生图工作流+自选模型+全节点注释_2084250496327577602.json, 图片生成/文生图/文生图第2课（B1）：SD2.1 768 高分辨率入门，comfyui从入门到躺平系列教程_1979377865538048002.json, 图片生成/文生图/文生图第3课SDXL Base 直出，comfyui从入门到躺平系列课程_1979390293403406337.json, 图片生成/文生图/文生图第5课 ：SDXL-Turbo 快速预览，comfyui从入门到躺平系列教程_1979445307241041922.json, 图片生成/文生图/文生图第6课：LCM-LoRA 加速任意 SD_SDXL，comfyui从入门到躺平系列教程_1979464950139752450.json, 图片生成/文生图/葬送的芙莉莲_1971514623306448898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（comfyui-workflow-templates-json/image_sdxl_simple.json、comfyui-workflow-templates-json/sdxl_revision_text_prompts.json、sd1.5/basic.json、图片生成/图生图/test_2060392964412764161.json、图片生成/图生图/文生图基础款_1980202895117291522.json…）

- **类型**：Text To Image
- **样本数**：36
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 36 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/36 个有
- `LoraLoaderModelOnly` —— 2/36 个有
- `CLIPVisionEncode` —— 1/36 个有
- `CLIPVisionLoader` —— 1/36 个有
- `CR Upscale Image` —— 1/36 个有
- `PreviewImage` —— 1/36 个有
- `unCLIPConditioning` —— 1/36 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 36 | 54% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 36 | 64% |
| 采样算法 | euler | - | 36 | 50% |
| 调度器 | karras | - | 36 | 44% |
| 重绘幅度 | 1 | 1 - 1 | 36 | 100% |
| 宽度 | 768 | 512 - 1920 | 36 | 65% |
| 高度 | 1024 | 512 - 1920 | 36 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/36 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，36 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，36 个样本
- 采样算法 最常用 euler，36 个样本，一致性 50%
- 调度器 最常用 karras，36 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 1 - 1，36 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 512 - 1920，36 个样本
- 高度 中位数 1024，观测区间 512 - 1920，36 个样本
