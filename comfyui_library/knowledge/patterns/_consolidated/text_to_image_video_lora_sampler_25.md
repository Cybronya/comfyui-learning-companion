---
name: text_to_image_video_lora_sampler_25
type: Text To Image
frequency: 23
level: strong
coverage: 0.711696
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json, 视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json, 视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json, 视频生成/文生视频/十二秒横屏文戏专用｜万象动漫短剧文生视频三模输入_2096618054703730690.json, 视频生成/文生视频/原版BF16高动态15秒｜Minimax H3 768P视频模板_2090880996274171906.json, 视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0 sage MinimaxH3文生视频图生视频_2088389915884220418.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088362225546391554.json, 视频生成/文生视频/双bf16满血版sage无损加速｜MinimaxH3文生图生视频生视频_2088371118150340610.json, 视频生成/文生视频/双bf16满血版｜MinimaxH3 8步lora 1.0+sage加速视频生成_2089460273106210818.json, 视频生成/文生视频/双时钟8步高质量极速多参V1｜Minimax文生图生视频生视频工作流_2087188424548769794.json, 视频生成/文生视频/双采去油腻中远景场景 MiniMax H3 文生视频画质清爽_2094173291773784066.json, 视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json, 视频生成/文生视频/多参考出片更稳｜MiniMax H3优化版人物角色视频_2096626000930103297.json, 视频生成/文生视频/多参考图输入视频生成 MiniMax H3优化版角色一致性更强_2104770269930934274.json, 视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json, 视频生成/文生视频/多参考生视频优化升级｜文生视频视频生视频一键生成_2095569186260078594.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3数字人图生视频_2095829921988964354.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3文生视频升级_2095564235781795841.json, 视频生成/文生视频/多图多音频参考生视频｜MiniMax H3无水印优化版_2095565882998222850.json, 视频生成/文生视频/官方全能参考版单采｜文生视频视频生视频图生视频｜三模式任选_2104778746879369218.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_25

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json、视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json、视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json、视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json、视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json…）

- **类型**：Text To Image
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 23 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 22/23 个有
- `KSamplerSelect` —— 22/23 个有
- `PrimitiveFloat` —— 21/23 个有
- `MiniMaxH3AVDecodeT8` —— 13/23 个有
- `CR Prompt Text` —— 12/23 个有
- `GetNode` —— 12/23 个有
- `MiniMaxH3AudioConditioningT8` —— 12/23 个有
- `SetNode` —— 12/23 个有
- `LTXVConcatAVLatent` —— 11/23 个有
- `LTXVSeparateAVLatent` —— 11/23 个有
- `MiniMaxH3ReferenceToVideo` —— 11/23 个有
- `MinimaxH3LatentUpscaler3D` —— 11/23 个有
- `Text` —— 10/23 个有
- `VAEDecodeAudio` —— 10/23 个有
- `SplitSigmas` —— 9/23 个有
- `LoadAudio` —— 8/23 个有
- `VHS_LoadVideo` —— 8/23 个有
- `easy float` —— 7/23 个有
- `Fast Groups Bypasser (rgthree)` —— 3/23 个有
- `LayerUtility: PurgeVRAM V2` —— 3/23 个有
- `Float` —— 2/23 个有
- `AudioSeparation` —— 1/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/23 个有
- `LoraLoaderBypassModelOnly` —— 1/23 个有
- `MiniMaxH3DualClockSamplerT8` —— 1/23 个有
- `PreviewImage` —— 1/23 个有
- `SaveImage` —— 1/23 个有
- `Text Multiline` —— 1/23 个有
- `图像缩放范围孤海` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 23 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 23 | 100% |
| 采样算法 | er_sde | - | 23 | 100% |
| 调度器 | beta | - | 23 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 23 | 100% |
| 宽度 | 80 | 80 - 80 | 23 | 100% |
| 高度 | 80 | 80 - 80 | 23 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/23 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，23 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，23 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，23 个样本，一致性 100%
- 调度器 最常用 beta，23 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，23 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，23 个样本，取值集中（一致性 100%）
- 高发问题（23/23 个样本）：Steps较低可能导致细节不足
