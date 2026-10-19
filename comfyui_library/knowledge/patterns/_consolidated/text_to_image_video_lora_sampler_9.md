---
name: text_to_image_video_lora_sampler_9
type: Text To Image
frequency: 28
level: strong
coverage: 0.68175
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json, 视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json, 视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json, 视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json, 视频生成/文生视频/十二秒横屏文戏专用｜万象动漫短剧文生视频三模输入_2096618054703730690.json, 视频生成/文生视频/原版BF16高动态15秒｜Minimax H3 768P视频模板_2090880996274171906.json, 视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0 sage MinimaxH3文生视频图生视频_2088389915884220418.json, 视频生成/文生视频/双bf16满血版8步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088362225546391554.json, 视频生成/文生视频/双bf16满血版sage无损加速｜MinimaxH3文生图生视频生视频_2088371118150340610.json, 视频生成/文生视频/双bf16满血版｜MinimaxH3 8步lora 1.0+sage加速视频生成_2089460273106210818.json, 视频生成/文生视频/双采去油腻中远景场景 MiniMax H3 文生视频画质清爽_2094173291773784066.json, 视频生成/文生视频/图MiniMax文生视频视频生视频图生视频_2085849570684260354.json, 视频生成/文生视频/多参考出片更稳｜MiniMax H3优化版人物角色视频_2096626000930103297.json, 视频生成/文生视频/多参考图输入视频生成 MiniMax H3优化版角色一致性更强_2104770269930934274.json, 视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json, 视频生成/文生视频/多参考生视频优化升级｜文生视频视频生视频一键生成_2095569186260078594.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3人物角色一致性_2096301587214987265.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3数字人图生视频_2095829921988964354.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3文生视频升级_2095564235781795841.json, 视频生成/文生视频/多参考生视频优化版｜角色一致性高质量视频生成_2095231061662978049.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2096723203140972545.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2097087018537938945.json, 视频生成/文生视频/多图多音频参考生视频｜MiniMax H3无水印优化版_2095565882998222850.json, 视频生成/文生视频/官方全能参考版单采｜文生视频视频生视频图生视频｜三模式任选_2104778746879369218.json, 视频生成/文生视频/知识分享单人视频生成器｜文生视频图生视频，口播内容快速成片_2104538809982603266.json, 视频生成/文生视频/虚空折叠流系列第四篇 H3最强二采方案效果超越SelfLift_2104827805753237506.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_9

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/文生视频/动作增强修复双采｜Minimax H3 b25-49参数版生成_2096314410406072321.json、视频生成/文生视频/动作增强修复｜MiniMax H3双采bf16精度稳定出片_2096530999692849154.json、视频生成/文生视频/动作增强修复｜MiniMax H3双采参数b25精细调校版_2096529451092889602.json、视频生成/文生视频/动漫多参考8步加速lora Minimax H3 Dasiwa 10步出片_2094220547021426689.json、视频生成/文生视频/动漫多参考直出1080P Minimax H3 Dasiwa文生视频_2094217735050973186.json…）

- **类型**：Text To Image
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
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
- `PrimitiveFloat` —— 26/28 个有
- `GetNode` —— 17/28 个有
- `LTXVConcatAVLatent` —— 17/28 个有
- `LTXVSeparateAVLatent` —— 17/28 个有
- `MiniMaxH3ReferenceToVideo` —— 17/28 个有
- `MinimaxH3LatentUpscaler3D` —— 17/28 个有
- `SetNode` —— 17/28 个有
- `VAEDecodeAudio` —— 16/28 个有
- `SplitSigmas` —— 15/28 个有
- `Text` —— 15/28 个有
- `LoadAudio` —— 14/28 个有
- `easy float` —— 13/28 个有
- `MiniMaxH3AVDecodeT8` —— 12/28 个有
- `VHS_LoadVideo` —— 12/28 个有
- `CR Prompt Text` —— 11/28 个有
- `MiniMaxH3AudioConditioningT8` —— 11/28 个有
- `忽略多组孤海` —— 4/28 个有
- `Fast Groups Bypasser (rgthree)` —— 3/28 个有
- `LayerUtility: PurgeVRAM V2` —— 3/28 个有
- `SaveImage` —— 3/28 个有
- `Float` —— 2/28 个有
- `Text Multiline` —— 2/28 个有
- `AudioSeparation` —— 1/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/28 个有
- `PreviewImage` —— 1/28 个有
- `图像缩放范围孤海` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 28 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 28 | 100% |
| 采样算法 | er_sde | - | 28 | 100% |
| 调度器 | beta | - | 28 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 28 | 100% |
| 宽度 | 80 | 80 - 80 | 28 | 100% |
| 高度 | 80 | 80 - 80 | 28 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/28 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，28 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，28 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，28 个样本，一致性 100%
- 调度器 最常用 beta，28 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，28 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，28 个样本，取值集中（一致性 100%）
- 高发问题（28/28 个样本）：Steps较低可能导致细节不足
