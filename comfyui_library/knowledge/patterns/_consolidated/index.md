# 归纳出的 Workflow 模式

> 本目录由 `engine/knowledge_consolidation` 自动生成，勿手改。
> 每个模式一个 Markdown 文件，frontmatter 存统计字段，正文存结论。

| 模式 | 类型 | 样本 | 可信度 | 覆盖 |
|---|---|---|---|---|
| [`sdxl_portrait_controlnet_lora_sampler`](sdxl_portrait_controlnet_lora_sampler.md) | SDXL Portrait | 4 | 强结论 | 85% |
| [`sd1_5_text2image_sampler_clip_checkpoint`](sd1_5_text2image_sampler_clip_checkpoint.md) | SD1.5 Text2Image | 3 | 强结论 | 100% |
| [`wan_text2video_video_sampler_clip`](wan_text2video_video_sampler_clip.md) | Wan Text2Video | 3 | 强结论 | 40% |

## 全局观察

- 必备节点（出现在 ≥80% 的 workflow，10 个样本）：CLIPTextEncode
- 少数派节点（出现率 <20%）：UpscaleModelLoader
- workflow 类型分布：SDXL Portrait 4 个、SD1.5 Text2Image 3 个、Wan Text2Video 3 个
- cfg 各模式中位数：sdxl_portrait_controlnet_lora_sampler 7.5、sd1_5_text2image_sampler_clip_checkpoint 7、wan_text2video_video_sampler_clip 5（sdxl_portrait_controlnet_lora_sampler 最高，wan_text2video_video_sampler_clip 最低，相差 2.5）
- steps 各模式中位数：wan_text2video_video_sampler_clip 55、sdxl_portrait_controlnet_lora_sampler 29、sd1_5_text2image_sampler_clip_checkpoint 22（wan_text2video_video_sampler_clip 最高，sd1_5_text2image_sampler_clip_checkpoint 最低，相差 33）

---

归纳自 10 个 workflow，形成 3 个模式
，生成时间 2026-10-06 01:46:25
