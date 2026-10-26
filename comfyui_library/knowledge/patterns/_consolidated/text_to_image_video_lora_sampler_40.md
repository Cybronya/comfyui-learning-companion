---
name: text_to_image_video_lora_sampler_40
type: Text To Image
frequency: 18
level: weak
coverage: 0.945556
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, EmptyLatentImage, INTConstant, ImageScaleBy, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, RIFE VFI, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2 Remix V3再来一版｜图生视频超流畅 角色设计更出彩_2105554155732561921.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频 超流畅最强版本_2098288411865083906.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频 超流畅美少女处理工具_2114085127751028738.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频-超流畅最强版工作流_2087380938660601858.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2108637087565176833.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109048079277187073.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2109185392078577666.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版，人物特效角色设计图生视频方案_2105798734188732418.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版｜角色设计动作丝滑_2101911432190316545.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频｜超流畅最强版丝滑运镜_2114042114505003010.json, 视频生成/图生视频/Wan2.2 Remix V3图生视频｜超流畅最强版滤镜特效_2108434989292548098.json, 视频生成/图生视频/Wan2.2 Remix V3极度丝滑图生视频处理生成工具_2102143798599045122.json, 视频生成/图生视频/Wan2.2 Remix V3超流畅图生视频｜人物一致性稳如老狗，动作不崩_2099542466520248321.json, 视频生成/图生视频/Wan2.2 Remix V3｜图生视频超流畅最强版 角色设计更出彩_2105509025721962497.json, 视频生成/图生视频/Wan2.2RemixV3极度丝滑没有之一图生视频ENGENGENG_2087117089000742914.json, 视频生成/图生视频/Wan2.2_原图加两套换装_带货视频_2075861551701127169.json, 视频生成/图生视频/Wan2.2_原图加两套换装_带货视频_2078711931518676993.json, 视频生成/文生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2105378477359845377.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Remix V3再来一版｜图生视频超流畅 角色设计更出彩_2105554155732561921.json、视频生成/图生视频/Wan2.2 Remix V3图生视频 超流畅最强版本_2098288411865083906.json、视频生成/图生视频/Wan2.2 Remix V3图生视频 超流畅美少女处理工具_2114085127751028738.json、视频生成/图生视频/Wan2.2 Remix V3图生视频-超流畅最强版工作流_2087380938660601858.json、视频生成/图生视频/Wan2.2 Remix V3图生视频超流畅最强版 动态生成优化_2108637087565176833.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `EmptyLatentImage`
- `INTConstant`
- `ImageScaleBy`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 16/18 个有
- `Text Concatenate` —— 16/18 个有
- `Wan22PromptSelector` —— 16/18 个有
- `solarL_SaveImagesToZip` —— 16/18 个有
- `孤海注释` —— 16/18 个有
- `SaveImage` —— 10/18 个有
- `GetImageSize` —— 2/18 个有
- `ImageBatchExtendWithOverlap` —— 2/18 个有
- `ImageScale` —— 2/18 个有
- `ImageScaleToTotalPixels` —— 2/18 个有
- `SeedVR2` —— 2/18 个有
- `TextEncodeQwenImageEditPlus` —— 2/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 18 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 18 | 73% |
| 采样算法 | er_sde | - | 18 | 89% |
| 调度器 | beta | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 720 | 18 | 0% |
| 高度 | 80 | 80 - 1280 | 18 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，18 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，18 个样本
- 采样算法 最常用 er_sde，18 个样本，一致性 89%
- 调度器 最常用 beta，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 720，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1280，18 个样本，取值分散，一致性仅 0%
- 高发问题（20/18 个样本）：Steps较低可能导致细节不足
