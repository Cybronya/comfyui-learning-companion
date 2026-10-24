---
name: text_to_image_video_upscale_latent_upscale
type: Text To Image
frequency: 22
level: strong
coverage: 0.592818
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3批量素材图生成｜支持文生图图生图工作流_2097442419775201281.json, 视频生成/文生视频/MiniMax+H3多参考生视频｜9图片3视频3音频任意混搭｜多角色锁定_2101896037253337090.json, 视频生成/文生视频/MiniMaxH3数字人带货视频｜多图生视频批量产出带货素材_2099148701758484482.json, 视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2094862928741756929.json, 视频生成/文生视频/lin多模态工作流｜文生视频视频生视频图生视频通吃_2101150805402406913.json, 视频生成/文生视频/万象AI与Singularity新模型｜12秒横屏960分辨率视频生成_2096669238164549633.json, 视频生成/文生视频/万象AI与Singularity新模型｜12秒竖屏960分辨率文生视频_2096667666223292417.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒横屏MiniMax H3制作_2096310040830496769.json, 视频生成/文生视频/万象动漫短剧文戏生成｜12秒竖屏多参视频制作_2096742818462134273.json, 视频生成/文生视频/十二秒横屏文戏专用｜万象动漫短剧文生视频三模输入_2096618054703730690.json, 视频生成/文生视频/多参考出片更稳｜MiniMax H3优化版人物角色视频_2096626000930103297.json, 视频生成/文生视频/多参考图输入视频生成 MiniMax H3优化版角色一致性更强_2104770269930934274.json, 视频生成/文生视频/多参考生视频优化升级｜文生视频视频生视频一键生成_2095569186260078594.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3人物角色一致性_2096301587214987265.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3数字人图生视频_2095829921988964354.json, 视频生成/文生视频/多参考生视频优化版｜MiniMax H3文生视频升级_2095564235781795841.json, 视频生成/文生视频/多参考生视频优化版｜角色一致性高质量视频生成_2095231061662978049.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2096723203140972545.json, 视频生成/文生视频/多参考生视频双采工作流｜MiniMax H3高清放大生成_2097087018537938945.json, 视频生成/文生视频/多图多音频参考生视频｜MiniMax H3无水印优化版_2095565882998222850.json, 视频生成/文生视频/知识分享单人视频生成器｜文生视频图生视频，口播内容快速成片_2104538809982603266.json, 视频生成/文生视频/虚空折叠流系列第四篇 H3最强二采方案效果超越SelfLift_2104827805753237506.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3批量素材图生成｜支持文生图图生图工作流_2097442419775201281.json、视频生成/文生视频/MiniMax+H3多参考生视频｜9图片3视频3音频任意混搭｜多角色锁定_2101896037253337090.json、视频生成/文生视频/MiniMaxH3数字人带货视频｜多图生视频批量产出带货素材_2099148701758484482.json、视频生成/文生视频/Minimax H3全能导演台｜短剧分镜丝滑衔接生成_2094862928741756929.json、视频生成/文生视频/lin多模态工作流｜文生视频视频生视频图生视频通吃_2101150805402406913.json…）

- **类型**：Text To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 22 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 21/22 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 21/22 个有
- `SetNode` —— 21/22 个有
- `SplitSigmas` —— 21/22 个有
- `easy float` —— 21/22 个有
- `LoadAudio` —— 17/22 个有
- `Text` —— 16/22 个有
- `VHS_LoadVideo` —— 16/22 个有
- `忽略多组孤海` —— 7/22 个有
- `Text Multiline` —— 5/22 个有
- `SaveImage` —— 4/22 个有
- `Lora Loader Stack (rgthree)` —— 2/22 个有
- `ModelAttentionBackend` —— 2/22 个有
- `SolAttnMiniMax` —— 2/22 个有
- `ExtractStoryboards_xuhuan1024` —— 1/22 个有
- `ManualSigmas` —— 1/22 个有
- `PrimitiveBoolean` —— 1/22 个有
- `VRAM_Debug` —— 1/22 个有
- `ZML_AnyTypeSwitch` —— 1/22 个有
- `llama_cpp_instruct_adv` —— 1/22 个有
- `llama_cpp_model_loader` —— 1/22 个有
- `llama_cpp_parameters` —— 1/22 个有
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
