---
name: text_to_image_video_lora_sampler_24
type: Text To Image
frequency: 22
level: strong
coverage: 0.578591
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json, 视频生成/文生视频/lin多模态工作流｜文生视频视频生视频图生视频通吃_2101150805402406913.json, 视频生成/文生视频/万象AI与Singularity新模型｜12秒横屏960分辨率视频生成_2096669238164549633.json, 视频生成/文生视频/万象AI与Singularity新模型｜12秒竖屏960分辨率文生视频_2096667666223292417.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒横屏MiniMax H3制作_2096310040830496769.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒竖屏多参视频制作_2096742818462134273.json, 视频生成/文生视频/十二秒横屏文戏专用｜万象动漫短剧文生视频三模输入_2096618054703730690.json, 视频生成/文生视频/双采去油腻中远景场景 MiniMax H3 文生视频画质清爽_2094173291773784066.json, 视频生成/文生视频/多参考出片更稳｜MiniMax H3优化版人物角色视频_2096626000930103297.json, 视频生成/文生视频/多参考图输入视频生成 MiniMax H3优化版角色一致性更强_2104770269930934274.json, 视频生成/文生视频/多参考生视频优化升级｜文生视频视频生视频一键生成_2095569186260078594.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3人物角色一致性_2096301587214987265.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3数字人图生视频_2095829921988964354.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3文生视频升级_2095564235781795841.json, 视频生成/文生视频/多参考生视频优化版｜角色一致性高质量视频生成_2095231061662978049.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2096723203140972545.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2097087018537938945.json, 视频生成/文生视频/多图多音频参考生视频｜MiniMax H3无水印优化版_2095565882998222850.json, 视频生成/文生视频/官方全能参考版单采｜文生视频视频生视频图生视频｜三模式任选_2104778746879369218.json, 视频生成/文生视频/电影质感V2｜MinimaxH3全能参考三模视频生成_2095082549973438466.json, 视频生成/文生视频/知识分享单人视频生成器｜文生视频图生视频，口播内容快速成片_2104538809982603266.json, 视频生成/文生视频/虚空折叠流系列第四篇 H3最强二采方案效果超越SelfLift_2104827805753237506.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_24

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json、视频生成/文生视频/lin多模态工作流｜文生视频视频生视频图生视频通吃_2101150805402406913.json、视频生成/文生视频/万象AI与Singularity新模型｜12秒横屏960分辨率视频生成_2096669238164549633.json、视频生成/文生视频/万象AI与Singularity新模型｜12秒竖屏960分辨率文生视频_2096667666223292417.json、视频生成/文生视频/万象动漫短剧文戏生成｜12秒横屏MiniMax H3制作_2096310040830496769.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MinimaxH3LatentUpscaler3D` —— 21/22 个有
- `PrimitiveFloat` —— 20/22 个有
- `SplitSigmas` —— 20/22 个有
- `VAEDecodeAudio` —— 20/22 个有
- `LTXVConcatAVLatent` —— 19/22 个有
- `LTXVSeparateAVLatent` —— 19/22 个有
- `LoadAudio` —— 18/22 个有
- `easy float` —— 18/22 个有
- `Text` —— 16/22 个有
- `VHS_LoadVideo` —— 16/22 个有
- `忽略多组孤海` —— 7/22 个有
- `Float` —— 4/22 个有
- `Text Multiline` —— 4/22 个有
- `SaveImage` —— 3/22 个有
- `Fast Groups Bypasser (rgthree)` —— 2/22 个有
- `Lora Loader Stack (rgthree)` —— 2/22 个有
- `MiniMaxH3AVDecodeT8` —— 2/22 个有
- `MiniMaxH3ConcatAVLatent` —— 2/22 个有
- `ModelAttentionBackend` —— 2/22 个有
- `SolAttnMiniMax` —— 2/22 个有
- `easy clearCacheAll` —— 2/22 个有
- `AudioSeparation` —— 1/22 个有
- `图像缩放范围孤海` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 22 | 100% |
| 采样算法 | er_sde | - | 22 | 100% |
| 调度器 | beta | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 80 | 80 - 80 | 22 | 100% |
| 高度 | 80 | 80 - 80 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，22 个样本，一致性 100%
- 调度器 最常用 beta，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
