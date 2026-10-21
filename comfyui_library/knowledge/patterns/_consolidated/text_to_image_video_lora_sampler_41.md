---
name: text_to_image_video_lora_sampler_41
type: Text To Image
frequency: 15
level: strong
coverage: 0.9232
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json, 视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json, 视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json, 视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json, 视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频 漫剧工作流，角色设计图生视频方案_2107927267103035393.json, 视频生成/图生视频/Minimax H3开源参考生视频创意视频短剧漫剧工作流，角色设计图生视频方案_2107965040040177666.json, 视频生成/图生视频/Minimax H3边跳边换装工作流｜图生视频动态效果生成_2097847006080356353.json, 视频生成/图生视频/Minimax H3边跳边换装｜舞蹈换装一镜到底_2097910210886197250.json, 视频生成/文生视频/万象文武双修均衡版｜12秒横屏多参视频生成制作_2096322789388144642.json, 视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json, 视频生成/文生视频/动漫短剧文武双修｜MiniMax H3双采参考生视频_2096309683601633281.json, 视频生成/文生视频/双采全能参考视频｜MiniMax H3真实电影质感文武均衡_2096297117051609090.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3文生视频极速二采高质量图ENGENG_2087151474047537153.json、视频生成/图生视频/MiniMax_H3视频复刻数字人｜视频换人换产品换文案语音替换_2110652655700889602.json、视频生成/图生视频/MiniMax_H3音频驱动数字人多人对话｜加速版长视频处理工具_2107983189108154369.json、视频生成/图生视频/Minimax H3动作增强修复双采｜高动态脸部兼顾_2098773573254082561.json、视频生成/图生视频/Minimax H3双时钟采样参考图生视频｜4步turbo极速出片_2111270718934708225.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 14/15 个有
- `孤海注释` —— 13/15 个有
- `LoraLoaderBypassModelOnly` —— 11/15 个有
- `MiniMaxH3DualClockSamplerT8` —— 11/15 个有
- `ModelAttentionBackend` —— 10/15 个有
- `SolAttnMiniMax` —— 9/15 个有
- `BasicScheduler` —— 5/15 个有
- `KSamplerSelect` —— 5/15 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 5/15 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 5/15 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 5/15 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 5/15 个有
- `LTXVConcatAVLatent` —— 4/15 个有
- `LTXVSeparateAVLatent` —— 4/15 个有
- `MinimaxH3LatentUpscaler3D` —— 4/15 个有
- `SaveImage` —— 4/15 个有
- `LoadAudio` —— 2/15 个有
- `StariAI-MiniMaxH3-Skill` —— 2/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `Label (rgthree)` —— 1/15 个有
- `PT_H3ConcatAVLatent` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `Text` —— 1/15 个有
- `VAEEncode` —— 1/15 个有
- `VHS_LoadVideo` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（16/15 个样本）：Steps较低可能导致细节不足
