---
name: text_to_image_video_lora_sampler_36
type: Text To Image
frequency: 18
level: strong
coverage: 0.897111
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json, 视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json, 视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json, 视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json, 视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json, 视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频 漫剧工作流，角色设计图生视频方案_2107927267103035393.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频短剧漫剧工作流，角色设计图生视频方案_2107965040040177666.json, 视频生成/图生视频/Minimax H3边跳边换装工作流｜图生视频动态效果生成_2097847006080356353.json, 视频生成/图生视频/Minimax H3边跳边换装｜舞蹈换装一镜到底_2097910210886197250.json, 视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json, 视频生成/图生视频/minimax商品视频展示 产品展示动态效果一键生成_2104643850022252545.json, 视频生成/图生视频/minimax商品视频展示｜图生视频电商产品动态主图制作_2104552227313639426.json, 视频生成/图生视频/双采加速图生视频｜MINIMAX-H3视频生成工作流_2088326770620715010.json, 视频生成/图生视频/双采加速工作流MINIMAX H3图生视频风扇变装模板_2088358447304761345.json, 视频生成/图生视频/最强Minimax商品视频展示工作流，图生视频电商产品展示处理工具_2108426664534433793.json, 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json, 视频生成/文生视频/文武双修均衡版｜MiniMax H3双采动漫短剧_2096624296683720706.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087143209582546946.json、视频生成/图生视频/MiniMax h3开源版H3图生视频短剧广告片创意视频口播MV跳舞视频生成数字人加速四倍_2087154037660672001.json、视频生成/图生视频/MiniMax-H3无限视频生成工作流｜分段接力长视频创作_2097784874290733057.json、视频生成/图生视频/MiniMax-H3音频驱动数字人多人对话加速版长视频处理工具.json、视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 17/18 个有
- `MiniMaxH3AVDecodeT8` —— 17/18 个有
- `MiniMaxH3AudioConditioningT8` —— 17/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 17/18 个有
- `RandomNoise` —— 17/18 个有
- `LoraLoaderBypassModelOnly` —— 15/18 个有
- `MiniMaxH3DualClockSamplerT8` —— 15/18 个有
- `孤海注释` —— 15/18 个有
- `CR Prompt Text` —— 12/18 个有
- `ModelAttentionBackend` —— 12/18 个有
- `SolAttnMiniMax` —— 11/18 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 8/18 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 8/18 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 8/18 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 8/18 个有
- `SaveImage` —— 7/18 个有
- `PrimitiveStringMultiline` —— 5/18 个有
- `BasicScheduler` —— 3/18 个有
- `ConcatTextOfUtils` —— 3/18 个有
- `KSamplerSelect` —— 3/18 个有
- `LoadAudio` —— 3/18 个有
- `PT_H3ConcatAVLatent` —— 3/18 个有
- `VAEDecodeAudio` —— 3/18 个有
- `VAEEncode` —— 3/18 个有
- `Fast Groups Bypasser (rgthree)` —— 2/18 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 2/18 个有
- `StariAI-MiniMaxH3-Skill` —— 2/18 个有
- `ImageResizeKJv2` —— 1/18 个有
- `Label (rgthree)` —— 1/18 个有
- `MiniMaxH3ReferenceToVideo` —— 1/18 个有
- `Text` —— 1/18 个有
- `workflow>运行采样` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高发问题（18/18 个样本）：Steps较低可能导致细节不足
