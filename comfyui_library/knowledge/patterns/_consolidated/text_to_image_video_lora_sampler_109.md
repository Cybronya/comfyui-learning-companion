---
name: text_to_image_video_lora_sampler_109
type: Text To Image
frequency: 6
level: strong
coverage: 0.848333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json, 数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json, 视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json, 视频生成/图生视频/MINIMAX多参官方加速工作流角色一致性图生视频热门IP_2087415478531743745.json, 视频生成/图生视频/海螺H3人物替换｜动作迁移角色一致性生成_2095271195703857153.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（数字人/数字人/MinimaxH3 角色替换｜视频换脸动作迁移数字人一键搞定_2096845137870671874.json、数字人/数字人/MinimaxH3角色替换工作流｜数字人换脸动作迁移生成_2096647400864706561.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成_2100304059428331521.json、视频生成/图生视频/H3导演台批量短剧专用4到9宫图视频生成工具_2100683233586401281.json、视频生成/图生视频/MINIMAX多参官方加速工作流角色一致性图生视频热门IP_2087415478531743745.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ReferenceToVideo` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `VAEDecodeAudio` —— 4/6 个有
- `easy int` —— 4/6 个有
- `GetImageSizeAndCount` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `ModelAttentionBackend` —— 3/6 个有
- `VHS_LoadVideo` —— 3/6 个有
- `VHS_VideoInfo` —— 3/6 个有
- `LoraLoaderBypassModelOnly` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `SFH3MultimodalDirector` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `Bookmark (rgthree)` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `Display Any (rgthree)` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `SimpleCalculatorKJ` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `StringReplace` —— 1/6 个有
- `TextGenerate` —— 1/6 个有
- `easy anythingIndexSwitch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
