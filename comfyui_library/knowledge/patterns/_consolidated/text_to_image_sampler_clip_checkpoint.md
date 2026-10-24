---
name: text_to_image_sampler_clip_checkpoint
type: Text To Image
frequency: 39
level: moderate
coverage: 0.897615
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/image_sdxl_simple.json, comfyui-workflow-templates-json/sdxl_revision_text_prompts.json, sd1.5/basic.json, 图片生成/图生图/test_2060392964412764161.json, 图片生成/图生图/文生图基础款_1980202895117291522.json, 图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json, 图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json, 图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json, 图片生成/文生图/SD_1971226483622658049.json, 图片生成/文生图/XL文生图基础款_1946346552236339202.json, 图片生成/文生图/Z-Image：Dark Beast Z⚡️ 红潮黑兽 AIO  V1.0_2007072752297054209.json, 图片生成/文生图/generate_image_2069748514313293826.json, 图片生成/文生图/动漫二次云_2100884264383504386.json, 图片生成/文生图/基础文生图_2013163381582209026.json, 图片生成/文生图/基础文生图工作流+全节点注释_2055473668087656449.json, 图片生成/文生图/夜色里的新中式建筑_2063975026935820290.json, 图片生成/文生图/宫崎骏风格文生图_2045321433018011649.json, 图片生成/文生图/少女漫特写镜头_2086340546775306242.json, 图片生成/文生图/少年热血漫画风_2099420731863031810.json, 图片生成/文生图/少年热血漫画风_2108742945393434625.json, 图片生成/文生图/少年热血漫画风_2110186250471821314.json, 图片生成/文生图/工作流基础篇-1-基础文生图工作流（SD1.5;SDXL）_2012411587696529410.json, 图片生成/文生图/抖音风视频生成_2039075658810265601.json, 图片生成/文生图/文生图基础款_1939591843099361281.json, 图片生成/文生图/文生图基础款_1944927998945714178.json, 图片生成/文生图/文生图基础款_1945720948937072641.json, 图片生成/文生图/文生图基础款_1947173020802265089.json, 图片生成/文生图/文生图基础款_1951180182470242305.json, 图片生成/文生图/文生图基础款_1962370527010623489.json, 图片生成/文生图/文生图学习款_1967328708090531841.json, 图片生成/文生图/文生图工作流 (1)_2052909337802231810.json, 图片生成/文生图/文生图工作流 (2)_2054023580740014082.json, 图片生成/文生图/文生图工作流+自选模型+全节点注释_2084250496327577602.json, 图片生成/文生图/文生图工作流_2052202461250760705.json, 图片生成/文生图/文生图第2课（B1）：SD2.1 768 高分辨率入门，comfyui从入门到躺平系列教程_1979377865538048002.json, 图片生成/文生图/文生图第3课SDXL Base 直出，comfyui从入门到躺平系列课程_1979390293403406337.json, 图片生成/文生图/文生图第5课 ：SDXL-Turbo 快速预览，comfyui从入门到躺平系列教程_1979445307241041922.json, 图片生成/文生图/文生图第6课：LCM-LoRA 加速任意 SD_SDXL，comfyui从入门到躺平系列教程_1979464950139752450.json, 图片生成/文生图/葬送的芙莉莲_1971514623306448898.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 39 个 workflow 归纳得出（comfyui-workflow-templates-json/image_sdxl_simple.json、comfyui-workflow-templates-json/sdxl_revision_text_prompts.json、sd1.5/basic.json、图片生成/图生图/test_2060392964412764161.json、图片生成/图生图/文生图基础款_1980202895117291522.json…）

- **类型**：Text To Image
- **样本数**：39
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 39 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/39 个有
- `LoraLoaderModelOnly` —— 2/39 个有
- `CLIPVisionEncode` —— 1/39 个有
- `CLIPVisionLoader` —— 1/39 个有
- `CR Upscale Image` —— 1/39 个有
- `PreviewImage` —— 1/39 个有
- `unCLIPConditioning` —— 1/39 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 60 | 39 | 56% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 39 | 69% |
| 采样算法 | euler | - | 39 | 54% |
| 调度器 | karras | - | 39 | 41% |
| 重绘幅度 | 1 | 1 - 1 | 39 | 100% |
| 宽度 | 768 | 480 - 1920 | 39 | 66% |
| 高度 | 1024 | 512 - 1920 | 39 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/39 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 60，39 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，39 个样本
- 采样算法 最常用 euler，39 个样本，一致性 54%
- 调度器 最常用 karras，39 个样本，一致性 41%
- 重绘幅度 中位数 1，观测区间 1 - 1，39 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 480 - 1920，39 个样本
- 高度 中位数 1024，观测区间 512 - 1920，39 个样本
