---
name: text_to_image_lora_sampler_clip_236
type: Text To Image
frequency: 8
level: strong
coverage: 0.866125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadVideo, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen3VL视频剧情反推｜上传视频自动还原提示词内容_2111762227706548226.json, 图片生成/反推提示词/gemini-3.5视频反推｜提示词自动提取视频理解反推工具_2088747131812270082.json, 图片生成/反推提示词/反推视频分镜脚本工作流，反推提示词视频分镜生成工具_2107975716578095106.json, 图片生成/反推提示词/反推视频分镜脚本神器｜一键拆解镜头方便复刻改编_2107689273460879361.json, 图片生成/反推提示词/反推视频提示词2.0｜从成片倒推可复用提示词模板_2107680507663314945.json, 图片生成/反推提示词/反推视频提示词2工作流，反推提示词视频分析处理工具_2107969731327258625.json, 图片生成/反推提示词/视频图像反推工作流｜反推提示词风格迁移 视频风格转换利器_2105563617381937153.json, 视频生成/文生视频/反推提示词｜视频反推工作流合集，一句话还原视频描述_2099874525914689538.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_236

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/反推提示词/Qwen3VL视频剧情反推｜上传视频自动还原提示词内容_2111762227706548226.json、图片生成/反推提示词/gemini-3.5视频反推｜提示词自动提取视频理解反推工具_2088747131812270082.json、图片生成/反推提示词/反推视频分镜脚本工作流，反推提示词视频分镜生成工具_2107975716578095106.json、图片生成/反推提示词/反推视频分镜脚本神器｜一键拆解镜头方便复刻改编_2107689273460879361.json、图片生成/反推提示词/反推视频提示词2.0｜从成片倒推可复用提示词模板_2107680507663314945.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `easy saveText` —— 7/8 个有
- `RH_LLMAPI_Pro_Node` —— 6/8 个有
- `ShowText|pysssss` —— 5/8 个有
- `easy showAnything` —— 4/8 个有
- `Qwen3VLProcessor` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `LayerFilter: FilmV2` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `NanguangTextToImage` —— 2/8 个有
- `PreviewAny` —— 2/8 个有
- `RH_Translator` —— 2/8 个有
- `easy positive` —— 2/8 个有
- `LoadImage` —— 1/8 个有
- `easy imageSave` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
