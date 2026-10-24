---
name: text_to_image_lora_sampler_clip_161
type: Text To Image
frequency: 10
level: strong
coverage: 0.9001
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Topaz Video星光放大工作流，视频超分高清增强方案_2103590475516174338.json, 图片生成/图生图/Topaz Video高清放大5分钟搞定｜30秒视频4k超分，视频超分性价比之选_2100468705477091329.json, 图片生成/图生图/Topaz Video高清放大工作流非星光版，视频超分分辨率提升方案_2103591945984634882.json, 图片生成/图生图/Topaz星光高清放大模型数毛党最爱地表最强放大模型，视频超分高清工具_2107545542661328897.json, 图片生成/图生图/Topaz星光高清放大模型视频超分处理工作流_2101390536962830338.json, 图片生成/图生图/Topaz星光高清放大模型｜数毛党最爱地表最强，视频超分拉满_2107366759350235137.json, 图片生成/图生图/VOSR 2.0视频高清放大 分辨率提升画质增强_2104993429301321729.json, 图片生成/图生图/VOSR 2.0视频高清放大｜视频超分画质翻倍｜老片修复清晰可见_2104769134167945217.json, 图片生成/图生图/VOSR 2.0视频高清放大｜超分修复一步到位_2097892476068646913.json, 图片生成/文生图/VOSR2超分放大 文生图高清增强处理工具_2098709966747160578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Topaz Video星光放大工作流，视频超分高清增强方案_2103590475516174338.json、图片生成/图生图/Topaz Video高清放大5分钟搞定｜30秒视频4k超分，视频超分性价比之选_2100468705477091329.json、图片生成/图生图/Topaz Video高清放大工作流非星光版，视频超分分辨率提升方案_2103591945984634882.json、图片生成/图生图/Topaz星光高清放大模型数毛党最爱地表最强放大模型，视频超分高清工具_2107545542661328897.json、图片生成/图生图/Topaz星光高清放大模型视频超分处理工作流_2101390536962830338.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `RH_Astra` —— 6/10 个有
- `RunningHub Deepcleaner` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `GetVideoComponents` —— 4/10 个有
- `VOSR2ModelLoader` —— 4/10 个有
- `VOSR2Upscale` —— 4/10 个有
- `DF_Integer` —— 3/10 个有
- `JWInteger` —— 3/10 个有
- `QZ_ResolutionPreset` —— 3/10 个有
- `SaveImage` —— 3/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `VHS_VideoInfoLoaded` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
