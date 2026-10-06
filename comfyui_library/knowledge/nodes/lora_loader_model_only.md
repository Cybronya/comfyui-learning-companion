# LoraLoaderModelOnly

## 节点类型

`LoraLoaderModelOnly`

## 分类

Model Loading

## 作用

只加载 LoRA 的模型权重部分，不改写文本编码器。

与完整的 `LoraLoader`（同时输出 MODEL 和 CLIP）不同，本节点
只有一条 MODEL 输入和一条 MODEL 输出，用在 DiT/Flow 类模型
（Qwen Image、Flux、Krea2 等）工作流里给底模叠加风格或角色 LoRA。

> 典型连接：`UNETLoader / CheckpointLoader` → MODEL →
> `LoraLoaderModelOnly` → MODEL → 采样器

## 参数（统计自 404 个真实 workflow，4883 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| lora_name | LoRA 文件名 | 任意 `.safetensors`，多为社区下载的角色/风格包 |
| strength_model | 模型权重强度 | **95% 的样本取 1.0**；其余集中在 0.5–0.9 |

## 常见问题与风险

- 多个本节点串叠时，最终强度是逐级相乘叠加，报错先检查链上每个 strength。
- strength > 1 常导致「Turbo 脸」畸变或画面崩坏；社区工作流习惯把
  解除安全限制类 LoRA 单独放在一个链上（见样本文件名提示）。
- 模型底模与 LoRA 的架构必须匹配（Qwen Image 的 LoRA 不能挂在 Flux 底模上）。

## 可信度

Generated（2026-10-06，由 workflow_learning 批量学习的参数统计自动起草，
参数分布为实测，作用描述为通行语义，未经人工逐字核对）TODO(待验证)
