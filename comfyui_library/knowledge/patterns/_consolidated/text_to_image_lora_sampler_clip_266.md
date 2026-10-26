---
name: text_to_image_lora_sampler_clip_266
type: Text To Image
frequency: 8
level: strong
coverage: 0.89075
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/人物提取一键分离｜数字人角色抠图素材提取工作流_2093834995659005953.json, 视频生成/图生视频/HappyHorse1.0图生视频 图像转视频快速处理工具_2114050074937487361.json, 视频生成/图生视频/Seedance2.0 Fast图生视频 快速动态视频生成_2110362092581769218.json, 视频生成/图生视频/Seedance2.0 Fast图生视频 快速图像转视频处理工具_2113368422968020993.json, 视频生成/图生视频/Vidu Q4 Preview参考生视频 高质量动态生成_2109390998626459650.json, 视频生成/图生视频/happyhorse1.0图生视频｜一张图就能生成动态片_2106626750871597057.json, 视频生成/图生视频/happyhorse1.0图生视频｜新模型图生视频尝鲜体验_2114082221207408641.json, 视频生成/图生视频/图生视频Seedance2.0 RunningHub企业版 高质量动态生成_2109033444645883906.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_266

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/人物提取一键分离｜数字人角色抠图素材提取工作流_2093834995659005953.json、视频生成/图生视频/HappyHorse1.0图生视频 图像转视频快速处理工具_2114050074937487361.json、视频生成/图生视频/Seedance2.0 Fast图生视频 快速动态视频生成_2110362092581769218.json、视频生成/图生视频/Seedance2.0 Fast图生视频 快速图像转视频处理工具_2113368422968020993.json、视频生成/图生视频/Vidu Q4 Preview参考生视频 高质量动态生成_2109390998626459650.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 7/8 个有
- `SaveImage` —— 6/8 个有
- `RH_AlibabaHappyhorse10ImageToVideo` —— 3/8 个有
- `RH_RhartVideoSparkvideo20FastImageToVideo` —— 3/8 个有
- `AddMask` —— 1/8 个有
- `ChinesePrompt_Mix` —— 1/8 个有
- `LayerMask: MaskPreview` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有
- `RH_ViduQ4PreviewReferenceToVideo` —— 1/8 个有
- `RMBG` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
